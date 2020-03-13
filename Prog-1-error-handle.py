
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException

try:
   req = requests.get('http://www.thelon.cm/xxx.htm',timeout=5)
   
   print(req.status_code)
except ReadTimeout:
  # 超时异常
  print('Timeout')
  # 需要把当前的url放到任务中，过一段时间再尝试连接
except ConnectionError:
  # 连接异常
  print('Connection error')
except RequestException:
  # 请求异常
  print('Error')
else:
  if req.status_code==200:
     print('访问正常！')
     #将爬取的网页req.text保存在本地
     
     fb=open("t.html","wb")    
     fb.write(req.content)
     fb.close()
  if req.status_code==404:
     print('页面不存在！')
     #把当前的url从爬虫任务中删除掉
  if req.status_code==403:
     print('页面禁止访问！')
  #...
