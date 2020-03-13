# -*- coding: utf-8 -*-
from urllib import parse
import requests
import json

# 调用users/show 接口
def get_pinfo(access_token,uid):
    # 用户个人信息字典
    pinfo_dict = {}
    url = 'https://api.weibo.com/2/users/show.json'
    url_dict = {'access_token': access_token, 'uid': uid}
    url_param = parse.urlencode(url_dict)    
    res=requests.get(url='%s%s%s' % (url, '?', url_param), headers=header_dict)
    
    decode_data = json.loads(res.text)
    pinfo_dict['昵称'] = decode_data['name']
    pinfo_dict['简介'] = decode_data['description']
    # 性别
    if decode_data['gender'] == 'f':
        pinfo_dict['性别'] = '女'
    elif decode_data['gender'] == 'm':
        pinfo_dict['性别'] = '男'
    else:
        pinfo_dict['性别'] = '未知'
    # 注册时间
    pinfo_dict['注册时间'] = decode_data['created_at']
    # 粉丝数
    pinfo_dict['粉丝数'] = decode_data['followers_count']
    # 关注数
    pinfo_dict['关注数'] = decode_data['friends_count']
    # 微博数
    pinfo_dict['微博数'] = decode_data['statuses_count']
    # 收藏数
    pinfo_dict['收藏数'] = decode_data['favourites_count']
    return pinfo_dict


if __name__ == '__main__':
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    # 填写access_token参数 与 uid,填写自己的
    access_token = '__________________'
    uid = '___________' #'7059060320'
    pinfo = get_pinfo(access_token,uid)
    for key, value in pinfo.items():
       print('{k}:{v}'.format(k=key, v=value))
