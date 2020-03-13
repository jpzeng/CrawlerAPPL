#coding:utf-8

from lxml import etree

html='<html><head><title>Test</title></head><body><h1 align="center">Big data news</h1><h1 align="center">AI news</h1><h1 align="right">2018.8.1</h1></body></html>'
content = etree.fromstring(html)
rows=content.xpath('/html/body/h1')
for row in rows:
  t=row.xpath('./text()')[0]
  print(t)



html = '<html><head><title>Test</title></head><body><table id="table1"cellspacing="0px"><tr><th>学号</th><th>姓名</th><th>成绩</th></tr><tr><td>1001</td><td>曾平</td><td>90</td></tr><tr><td>1002</td><td>王一</td><td>92</td></tr><tr><td>1003</td><td>张三</td><td>88</td></tr></table></body></html>'
content = etree.HTML(html)
rows = content.xpath('//table[@id="table1"]/tr')[1:]
for row in rows:
   id = row.xpath('./td[1]/text()')[0]
   name = row.xpath('./td[2]/text()')[0]
   score = row.xpath('./td[3]/text()')[0]
   print(id, name, score)


                                                
print("演示提示最后一个记录")
html = '''<html><head><title>Test</title></head><body><table id="table1"cellspacing="0px"><tr><th>学号</th><th>姓名</th><th>成绩</th></tr>
<tr><td>1001</td><td>曾平</td><td>90</td></tr>
<tr><td>1002</td><td>王一</td><td>92</td></tr>
<tr><td>1003</td><td>张三</td><td>88</td></tr>
</table></body></html>'''

content = etree.HTML(html)
rows = content.xpath('//table[@id="table1"]/tr[last()]')
for row in rows:
   id = row.xpath('./td[1]/text()')[0]
   name = row.xpath('./td[2]/text()')[0]
   score = row.xpath('./td[3]/text()')[0]
   print(id, name, score)

