

# python3.6环境
import requests
import re

#从浏览器的开发者模式复制Cookie，保存到文本文件taobao-hk.txt
f=open(r'taobao-dd.txt','r')  #打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'):   #按照字符：进行划分读取    #其设置为1就会把字符串拆分成2份    
     name,value=line.strip().split('=',1)    
     cookies[name]=value  #为字典cookies添加内容

r=requests.get("https://www.taobao.com/",cookies=cookies)
#print(r.text)
rs=re.findall(u'<title>.*</title>',r.text)  #<title>淘宝网 - 淘！我喜欢</title>
print(rs)

