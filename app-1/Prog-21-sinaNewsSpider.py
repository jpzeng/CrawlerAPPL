# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import traceback
import os
import re


# 抓取新闻页面信息,返回新闻dict和图片list
def get_news(new_url):
    # 新闻信息字典
    new_dict = {}
    print("新闻地址: " + new_url)
    try:
        res = requests.get(new_url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')
        # 标题
        new_title = soup.select('h1.main-title')[0].text.strip()
        new_dict['title'] = new_title
        # 时间
        nt = datetime.strptime(soup.select('span.date')[0].text.strip(), '%Y年%m月%d日 %H:%M')
        new_time = datetime.strftime(nt, '%Y-%m-%d %H:%M')
        new_dict['time'] = new_time
        # 来源 不能使用a.source 个别网页来源内容所在标签为span标签
        new_source = soup.select('.source')[0].text
        new_dict['source']  = new_source
        # 作者
        new_author = soup.select('p.show_author')[0].text
        new_dict['author'] = new_author
        # 正文
        news_article = soup.select('div#article > p')
        tmp_str = ''
        for i in range(len(news_article)-1):
            tmp_str += news_article[i].text + '\r\n'
        new_dict['article'] = tmp_str
        # 图片
        news_pic = soup.select('div.img_wrapper > img')
        news_pic_list = []
        for pic in news_pic:
            news_pic_list.append(pic.get("src"))
        new_dict['picture'] = news_pic_list
    except Exception as e:
        print('抓取出错，此条新闻已略过')
        print(e)
        traceback.print_exc()
        return None, None
    print('时间:%s 标题:%s 作者:%s 来源:%s ' % (new_time, new_title, new_author, new_source))
    print('共有%d张图片' % len(news_pic_list))
    return new_dict, news_pic_list


# 获取所有新闻链接
def get_url_list(new_list_url):
    # 新闻链接list
    news_url_list = []
    # 通过range 控制爬取页数或爬完为止
    for i in range(1, 3):
        url = new_list_url.format(page=i)
        tmp_url_list = get_url(url)
        # 合并url列表
        if len(tmp_url_list):
            news_url_list[len(news_url_list):len(news_url_list)] = tmp_url_list
        else:
            print('-----------目录爬取完毕-----------')
            break
    return news_url_list


# 获取指定页的所有新闻链接
def get_url(new_list_url):
    url = new_list_url
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # 获取新闻链接
    url_list = []
    news_url = soup.select('ul.list_009 > li > a')
    for url in news_url:
        url_list.append(url.get('href'))
    print('本页共%d条新闻 链接:%s' % (len(url_list), new_list_url))
    return url_list


# 保存新闻
def save_new(root_dir, news_dict, pic_list):
    # 创建子文件夹
    try:
        # 路径名中不能出现一些符号，需要进行过滤
        title = news_dict['title']
        title = re.sub(r'[\\/:*?"<>|!：？！；]', '_', title)
        file_dir = root_dir + os.sep + title
        is_dir_exist = os.path.exists(file_dir)
        if not is_dir_exist:
            os.makedirs(file_dir)
        # 输出新闻文本
        save_text(file_dir, news_dict)
        # 输出图片
        save_pic(file_dir, pic_list)
    except Exception as e:
        print('保存出错')
        print(e)
        traceback.print_exc()
    print("保存完毕，新闻文件路径:%s" % file_dir)


# 保存文本
def save_text(file_dir, news_dict):
    res = ('标题:' + news_dict['title'] + '\r\n' +
           '时间:' + news_dict['time'] + '\r\n' +
           '作者:' + news_dict['author'] + '\r\n' +
           '来源:' + news_dict['source'] + '\r\n' +
           '新闻正文:' + news_dict['article'] + '\r\n ')
    # 文件名中不能出现一些符号，需要进行过滤
    title = news_dict['title']
    title = re.sub(r'[\\/:*?"<>|!：？！；]', '_', title)
    # 输出
    file_path = file_dir + os.sep + title + '.txt'
    f = open(file_path, "wb")
    f.write(res.encode("utf-8"))
    f.close()


# 保存图片
def save_pic(file_dir, pic_list):
    for i in range(len(pic_list)):
        # 图片保存路径
        pic_path = file_dir + os.sep + '%d.jpg' % i
        try:
            req = requests.get(pic_list[i])
        except requests.exceptions.MissingSchema as e:
            print('图片URL出错,尝试补全URL')
            print(e)
            req = requests.get('http:' + pic_list[i])
        finally:
            img = req.content
            f = open(pic_path, "wb")
            f.write(img)


# 开始执行
def start_spider(root_url, root_dir):
    url_list = get_url_list(root_url)
    print('----链接获取结束----')
    print('即将抓取 %d 条新闻\r\n' % len(url_list))
    for i in range(len(url_list)):
        print('%d: ' % i)
        new, pic = get_news(url_list[i])
        if new:
            save_new(root_dir, new, pic)
    print('--------抓取结束--------')


if __name__ == '__main__':
    # 入口 {page}用于format格式化
    root_url = 'http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_{page}.shtml'
    root_dir = r'.\news'
    start_spider(root_url, root_dir)
