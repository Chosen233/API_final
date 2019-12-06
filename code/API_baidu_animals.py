
# coding: utf-8

# # 百度AI动物识别API

# In[3]:


# encoding:utf-8

import requests
import base64

'''
动物识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
# 二进制方式打开图片文件
f = open('/Users/panzhuoqi/Downloads/tiger.jpeg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.36a15d69223ce6e587b7428f53e0111a.2592000.1578017218.282335-17924750'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())

