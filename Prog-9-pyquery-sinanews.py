# -*- coding: utf-8 -*-
from pyquery import PyQuery

html='''
<html><body><div id="second-title">访华前 这个国家的总理说“感谢中国体谅”</div>
<div class="date-source">
<span class="date">2019年03月27日 21:30</span></div>
<span class="publish source">参考消息</span>
<div class="article">
<p>原标题：锐参考 | 访华前，这个国家的总理说：“感谢中国体谅！”</p>
<p>“非常感谢中国的理解！”</p>
<p>在25日的新闻发布会上，新西兰总理杰辛达·阿德恩这样说道。</p>
</div>
</body></html>
'''
py = PyQuery(html)

#id名前加#
title = py('div#second-title')[0].text 

#类名(class)前加点
date=py('span.date')[0].text

#类名中的空格用点替换，即publish.source
source=py('span.publish.source')[0].text 

#子标签通过 > 定义
content = py('div.article > p') 
contentstr = ''
for i in range(len(content)):
  contentstr += content[i].text+"\n"

print("标题：",title)
print("发布日期：",date)
print("消息来源：",source)
print("消息内容：", contentstr)


xs=py('body').find('div')
d=xs(".date-source .date")
print(d[0].text)
