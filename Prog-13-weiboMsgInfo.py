# -*- coding: utf-8 -*-
from urllib import parse
import requests
import json

# 调用statuses/show 接口
def get_weibo(access_token, wid,header_dict):
    url = 'https://api.weibo.com/2/statuses/show.json'
    url_dict = {'access_token': access_token, 'id': wid}
    url_param = parse.urlencode(url_dict)
    res=requests.get(url='%s%s%s' % (url, '?', url_param), headers=header_dict)
    decode_data = json.loads(res.text)
    text = decode_data['text']
    if 'retweeted_status' in decode_data:
        text += '     <---原始微博：'+decode_data['retweeted_status']['text']
    return text

# 调用statuses/user_timeline/ids 接口
def get_weiboid(access_token,header_dict):
    url = 'https://api.weibo.com/2/statuses/user_timeline/ids.json'
    url_dict = {'access_token': access_token}
    url_param = parse.urlencode(url_dict)
    #req = request.Request(url='%s%s%s' % (url, '?', url_param), headers=header_dict)
    #res = request.urlopen(req)
    #res = res.read()
    res=requests.get(url='%s%s%s' % (url, '?', url_param), headers=header_dict)
    decode_data = json.loads(res.text)
    wid_list = decode_data['statuses']
    return wid_list

header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
# 填写access_token参数,请填写自己的access_token
access_token = '__________________' 
wid_list = get_weiboid(access_token=access_token, header_dict=header_dict)
# 输出博文
for item in wid_list:
    weibo_text = get_weibo(access_token=access_token, wid=item, header_dict=header_dict)
    print('微博id:'+str(item)+'--->'+weibo_text+'\n')
print('获取结束\n')
