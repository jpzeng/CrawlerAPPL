# -*- coding: utf-8 -*-
import html5lib

print('通过指定treebuilder来解析：')
document='<html><head><title>Test</title></head><body><h1 align="center">Big data news</h1><h1 align="center">AI news</h1><h1 align="right">2018.8.1</h1></body></html>'
#直接调用html5lib.parse来解析，解析时采用lxml构建树的方法
content=html5lib.parse(document,treebuilder="lxml",namespaceHTMLElements=False)
#指定要提取的内容所在的标签路径
rows=content.xpath('/html/body/h1')
for row in rows:
  t=row.xpath('./text()')[0]    #定位到标签节点后，通过text()提取内容
  print(t)


print('通过指定tree来解析：')
document='<html><head><title>Test</title></head><body><h1 align="center">Big data news</h1><h1 align="center">AI news</h1><h1 align="right">2018.8.1</h1></body></html>'
#构造HTMLParser实例，指定构造lxml的树
p=html5lib.HTMLParser(strict=False,tree=html5lib.getTreeBuilder('lxml'),namespaceHTMLElements=False)
#解析HTML文档
t=p.parse(document)
rows=t.xpath('/html/body/h1')
for row in rows:
  t=row.xpath('./text()')[0]
  print(t)

print('通过指定tree来提取超链接：')
document='<html><head><title>Test</title></head><body><a href="www.baidu.com">baidu</body></html>'
p=html5lib.HTMLParser(strict=False,tree=html5lib.getTreeBuilder('lxml'),namespaceHTMLElements=False)
t=p.parse(document)
#通过findall来查找所有标签名称为a的节点
a_tags = t.findall(".//a")
for a in a_tags:
   url = a.attrib["href"]   #通过属性名称来获得属性值
   print(url)

print('处理标签不完整或有错误的HTML：')
#这个HTML文档中有不完整的标签：缺少一个</h1>、有错误的标签：</m1>
document='<html><head><title>Test</title></head><body><h1 align="center">Big data news</h1><h1 align="center">AI news<h1 align="right">2018.8.1</m1></body></html>'
p=html5lib.HTMLParser(strict=False,tree=html5lib.getTreeBuilder('lxml'),namespaceHTMLElements=False)
t=p.parse(document)
rows=t.xpath('/html/body/h1')
for row in rows:
  t=row.xpath('./text()')[0]
  print(t)
