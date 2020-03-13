# encoding=utf-8
from bs4 import BeautifulSoup
import requests
import re
import time
import UrlSequence as urls


class Crawler:
    def __init__(self, base_url):
        # 初始化任务
        self.UrlSequence = urls.UrlSequence()
        # 增加种子URL，作为未爬行任务
        self.UrlSequence.Unvisited_Add(base_url)
        print ("Add the base url \"%s\" to the unvisited url list" % str(self.UrlSequence.unvisited))

    # 爬行的主过程
    def crawling(self, base_url, max_count, flag):
        # 当爬行任务非空，并且爬行的页面没有超过设定值时， 一直爬行
        while self.UrlSequence.UnvisitedIsEmpty() is False and self.UrlSequence.Visited_Count() <= max_count:
            # 对于宽度优先或深度优先，分别使用Dequeue，pop
            if flag == 1:  # using BFS
                visitUrl = self.UrlSequence.Unvisited_Dequeue()
            else:  # using DFS
                visitUrl = self.UrlSequence.Unvisited_Pop()
            print ("Pop out one url \"%s\" from unvisited url list" % visitUrl)
            if visitUrl in self.UrlSequence.visited or visitUrl is None or visitUrl == "":
                continue

            # 抓取页面，并提取页面中的超链接到links中
            links = self.getLinks(visitUrl)
            print ( "Get %d new links" % len(links))

            # 保存到已抓取的任务中
            self.UrlSequence.Visited_Add(visitUrl)
            print ("Visited url count: " + str(self.UrlSequence.Visited_Count()))

            # 将新提取出的超链接保存到未抓取的任务中
            for link in links:
                self.UrlSequence.Unvisited_Add(link)
            print ("%d unvisited links:" % len(self.UrlSequence.getUnvisitedUrl()))

    # 获得URL页面中的超链接
    def getLinks(self, url):
        links = []             #保存超链接的列表
        data = self.getPageSource(url)
        if data[0] == "200":
            # Create a BeautifulSoup object
            soup = BeautifulSoup(data[1],'lxml')
            # 通过 <a href=".*"> 查找超链接
            a = soup.findAll("a", {"href": re.compile(".*")})
            for href in a:
                if href["href"].find("http://") != -1 or href["href"].find("https://") != -1:
                    links.append(href["href"])
        return links

    # 获得URL对应的HTML源码
    def getPageSource(self, url, timeout=100, coding=None):
        try:
            #如果要设定多个headers属性，用逗号隔开
            page=requests.get(url, headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'})
            page.encoding='utf-8'
            html=page.text

            #保存文件,取当前系统时间戳作为文件名
            file_name =   '%d'%time.time() + '.htm'
            f = open(file_name, "wb")
            f.write(html.encode("utf-8"))  #编码成字节
            f.close()


            return ["200", html]
        except Exception as e:
            print ('错误：'+str(e))
            return [str(e), None]
