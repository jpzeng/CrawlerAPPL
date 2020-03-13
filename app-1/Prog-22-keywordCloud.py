# -*- coding: utf-8 -*-

import jieba
import os
import chardet
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread

# 设置新闻文本根目录、图像路径
newsTextdir = r'.\news'
img_path = r'.\background.jpg'
stop_word_path = r'.\stopword.txt'
my_word_path = r'.\myword.txt'

# 增加停用词库
def add_stop_words(list):
    stop_words = set()
    for item in list:
        stop_words.add(item.strip())
    return stop_words

def getnewstext(newsdir):
  news_text=""
  sd=os.walk(newsdir)
  for d,s,fns in sd:
     for fn in fns:
          if fn[-3:]=='txt':
               file=d+os.sep+fn
               print(file)
               try:
                  f=open(file)
                  lines=f.readlines()
               except:
                  ft=open(file,"rb")
                  cs=chardet.detect(ft.read())
                  ft.close()
                  f=open(file,encoding=cs['encoding'])
                  lines=f.readlines()
               for i in range(len(lines)):
                  news_text+='.'.join(lines)
  return news_text

# 读取文本和背景图片,rb即二进制读取
stopword_list = open(stop_word_path, encoding='utf-8').readlines()
myword_list = open(my_word_path, encoding='utf-8').readlines()
bg_img = imread(img_path)
news_text=getnewstext(newsTextdir)
                  
# 设置停用词
stop_words = add_stop_words(stopword_list)
print('停用词共:', stop_words.__len__())

# 加载自定义词库
jieba.load_userdict(my_word_path)

# 切分文本
seg_list = jieba.cut(news_text)
seg_space = ' '.join(seg_list)

# 生成词云，font_path需指向中文字体以避免中文变成方框，若出现非方框的乱码则为txt读取时的编码选择错误
wc = WordCloud(font_path='C:\Windows\Fonts\simfang.ttf', max_words=40, random_state=42,background_color='white', stopwords=stop_words,
               mask=bg_img, max_font_size=100, scale=5, collocations=False).generate(seg_space)
plt.imshow(wc)
#image_color = ImageColorGenerator(bg_img)
#plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()

# 保存结果
wc.to_file('.\wordcloud_res.jpg')

