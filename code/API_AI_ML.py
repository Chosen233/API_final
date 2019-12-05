
# coding: utf-8

# # 百度AI动物识别API

# In[7]:


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


# In[5]:


# 调用token
# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ePM54d7oGji4jfGKVAMNZAct&client_secret=lSzTRUvqGHsq5Pd42XaH8VhEXB7IcRXk'
response = requests.get(host)
if response:
    print(response.json())


# # 百度AI植物识别API

# In[7]:


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/Users/panzhuoqi/Downloads/cpc.png')

""" 调用植物识别 """
client.plantDetect(image);

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用植物识别 """
client.plantDetect(image, options)


# {
# 	"log_id": "7347136399676234884",
# 	"result": [
# 		{
# 			"score": 0.80000001192093,
# 			"name": "杜鹃花"
# 		},
# 		{
# 			"score": 0.45754179358482,
# 			"name": "高山杜鹃"
# 		},
# 		{
# 			"score": 0.023442218080163,
# 			"name": "杜鹃"
# 		},
# 		{
# 			"score": 0.021984783932567,
# 			"name": "美容杜鹃"
# 		},
# 		{
# 			"score": 0.020700372755527,
# 			"name": "黄山杜鹃"
# 		}
# 	]
# }

# #  百度AI语音合成API

# In[5]:


from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '17924750'
API_KEY = 'ePM54d7oGji4jfGKVAMNZAct'
SECRET_KEY = 'lSzTRUvqGHsq5Pd42XaH8VhEXB7IcRXk'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# In[6]:


result  = client.synthesis('你好百度', 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)


# In[17]:


# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化要请求产品(以cvm为例)的client对象
    client = cvm_client.CvmClient(cred, "ap-shanghai")

    # 实例化一个请求对象
    req = models.DescribeZonesRequest()

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeZones(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)


# # 百度AI通用物体识别API

# In[4]:


from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '17924750'
API_KEY = 'ePM54d7oGji4jfGKVAMNZAct'
SECRET_KEY = 'lSzTRUvqGHsq5Pd42XaH8VhEXB7IcRXk'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/Users/panzhuoqi/Downloads/glasses.jpeg')

""" 调用通用物体识别 """
client.advancedGeneral(image);

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用通用物体识别 """
client.advancedGeneral(image, options)


# # 百度语音合成API

# In[1]:


from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '17924750'
API_KEY = 'ePM54d7oGji4jfGKVAMNZAct'
SECRET_KEY = 'lSzTRUvqGHsq5Pd42XaH8VhEXB7IcRXk'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# In[7]:


# coding=utf-8
import sys
import json

IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

API_KEY = '4E1BG9lTnlSeIf1NQFlrSq6h'
SECRET_KEY = '544ca4657ba8002e3dea3ac2f5fdd241'

TEXT = "大潘今天也要加油哦"

# 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
# 精品音库：5为度小娇，103为度米朵，106为度博文，110为度小童，111为度小萌，默认为度小美 
PER = 4
# 语速，取值0-15，默认为5中语速
SPD = 5
# 音调，取值0-15，默认为5中语调
PIT = 5
# 音量，取值0-9，默认为5中音量
VOL = 5
# 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
AUE = 3

FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[AUE]

CUID = "123456PYTHON"

TTS_URL = 'http://tsn.baidu.com/text2audio'


class DemoError(Exception):
    pass


"""  TOKEN start """

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选


def fetch_token():
    print("fetch token begin")
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()

    print(result_str)
    result = json.loads(result_str)
    print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not SCOPE in result['scope'].split(' '):
            raise DemoError('scope is not correct')
        print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


"""  TOKEN end """

if __name__ == '__main__':
    token = fetch_token()
    tex = quote_plus(TEXT)  # 此处TEXT需要两次urlencode
    print(tex)
    params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

    data = urlencode(params)
    print('test on Web Browser' + TTS_URL + '?' + data)

    req = Request(TTS_URL, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()

        headers = dict((name.lower(), value) for name, value in f.headers.items())

        has_error = ('content-type' not in headers.keys() or headers['content-type'].find('audio/') < 0)
    except  URLError as err:
        print('asr http response http code : ' + str(err.code))
        result_str = err.read()
        has_error = True

    save_file = "error.txt" if has_error else 'result.' + FORMAT
    with open(save_file, 'wb') as of:
        of.write(result_str)

    if has_error:
        if (IS_PY3):
            result_str = str(result_str, 'utf-8')
        print("tts api  error:" + result_str)

    print("result saved as :" + save_file)

