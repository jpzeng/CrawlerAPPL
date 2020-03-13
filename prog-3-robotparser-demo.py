import urllib.robotparser
import requests

#读取robots.txt文件
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://item.taobao.com/robots.txt")
rp.read()

#模拟Googlebot，能生成文件
useragent='Googlebot'  
#模拟Baiduspider，不能生成文件
#useragent='Baiduspider'
url='https://item.taobao.com/item.htm?spm=a219r.lm897.14.38.5d2346e28rO73l&id=522811099442&ns=1&abbucket=7'
if rp.can_fetch(useragent, url):
  print("允许抓取")
  file=requests.get(url)
  data=file.content         #读取全部
  fb=open("bd-html","wb")    #将爬取的网页保存在本地
  fb.write(data)
  fb.close()
else:
  print("不允许抓取")


