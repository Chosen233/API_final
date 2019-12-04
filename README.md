# 项目名称：一起开眼界
# Product Requirement（产品说明文档）

| Title                     | Content |
| ------------------------- | ------- |
| Target release(发布日期)  | 2019/11 |
| Epic(史诗名称)            | 一起开眼界 |
| Document status(文档状态) | 进行中  |
| Document owner(文件主人)  | 潘卓祺  |
| Designer(领头的设计师)    | 潘卓祺  |
| Developer(领头的开发者)   | 潘卓祺  |
| QA(领头的测试者)          | 潘卓祺  |

# Catalogue（目录）
- [PRD1加值宣言](#加值宣言)
- [PRD2核心价值](#核心价值)
- [PRD3核心价值与用户痛点](#核心价值与用户痛点)
- [PRD4人工智能概率性与用户痛点](#人工智能概率性与用户痛点)
- [PRD5需求列表与人工智能API加值](#需求列表与人工智能API加值)


## 产品定位
本产品旨在为1-12岁的幼年儿童以及幼年儿童的家长提供的一款全面的大自然科普学习软件。


## 背景
- 1-12岁的幼年儿童正处于吸收知识的时候，对大自然的一切因素都感到非常的好奇。有时候家长因为不了解／不知道而不能回答出自己孩子提出的问题（如：这是什么动物、这是什么植物等）

- 通过对一系列的识别APP调查，几乎所有的APP目标用户都偏向幼年儿童以上，没有一款是针对幼年儿童设计的科普APP
    - 科普类的APP又不支持拍照识别功能

- 目前市场上有几个能识别动植物的APP：
    - “动物识别器APP”：只能通过拍照识别动物，不能通过文字搜索动物。
    - 点开了解动物详情后，页面跳转到百度百科。对于幼年儿童来说，年龄较低的儿童，识字能力有限，所以不能很好的阅读完全部内容。
    - “全能识别王”：百度AI上的图像识别功能几乎都用上了，也是只能通过拍照识别，不支持文字搜索。
  
# PART1 PRD价值主张设计

## 加值宣言

本产品皆在通过使用人工只能的部分功能（图像识别、语音识别、语音合成）来实现更好的大自然科普效果。

- （主要）百度AI的动物识别API对本产品价值部分在于：识别近八千种动物，接口返回动物名称，并获取百科信息，适用于拍照识图类APP中。
   
- （主要）百度AI的植物识别API对本产品价值部分在于：支持识别超过2万种通用植物和近8千种花卉，接口返回植物的名称，并获取百科信息，适用于拍照识图类APP中。
 
- （辅助）语音合成API对本产品价值部分在于：高度拟人、流畅自然的语音合成，提供多场景音库；语速、音调可调节；支持多音字标注。

- （辅助）语音识别API对本产品价值部分在于：将语音快速准确识别为文字，支持手机应用语音交互、语音内容分析、机器人对话等多个场景。

## 核心价值
- 语音合成：最小可用产品为能够实现有声读物功能
- 语音识别：最小可用产品为能够准确识别博物馆管理员的介绍，将60s以内的语音精准识别为文字。
- 动物识别：最小可用产品为拍照／上传动物的图片，返回该动物的名称、详细信息及可信度。
- 植物识别：最小可用产品为为拍照／上传植物的图片，返回该植物的名称、详细信息及可信度。


## 核心价值与用户痛点
- 在外活动的时候，家长想教育孩子识植物／动物时偶尔会遇到不认识的植物／动物，无法给孩子进行详细的说明。
- 家长想用更加有趣的方式给孩子进行科普，而不想用枯燥的传统方式给孩子进行教育。
- 在幼年儿童单独使用的时候，会遇到不认识的字。


## 人工智能概率性与用户痛点
- 照片清晰度较好的时候
- 照片模糊，同类型不同品种的动物识别成功率较低。对于在移动中的用户来说不太友好。

    - 西伯利亚虎原图
    ![动物识别](https://images.gitee.com/uploads/images/2019/1203/204953_342b473c_1532279.png "屏幕快照 2019-12-03 20.49.27.png")
    
    - 模糊后
    ![模糊后](https://images.gitee.com/uploads/images/2019/1203/205627_4bfb5eee_1532279.png "屏幕快照 2019-12-03 20.55.57.png")
    

## 需求列表与人工智能API加值

需求列表

| #   | User Story（用户案例）                                                         | Importance（重要性） | Notes（笔记） | 技术     |
| --- | ------------------------------------------------------------------------------ | -------------------- | ------------- | -------- |
| 1   | 李女士带小明在外游玩，小明问李女士这是什植物，李女士不清楚，无法回答小明的问题 | 极其重要             | 核心功能      | 植物识别 |
| 2   | 李女士带小明在外游玩，小明问李女士这是什动物，李女士不清楚，无法回答小明的问题 | 极其重要             | 核心功能      | 动物识别 |
| 3   | 小明在单独使用该APP遇到不认识的字，自己也没有学过拼音，周围也没有大人在        | 重要                 | 辅助功能      | 语音合成 |
| 4   | 李女士不想输入文字，想通过语音功能来查找动物／植物                                 | 重要                 | 辅助功能      | 语音识别 |
| 5   | 林先生的普通话不标准，容易误导自己的小孩                                       | 重要                 | 辅助功能      | 语音合成 |

## 产品架构图
![产品架构图](https://images.gitee.com/uploads/images/2019/1203/233301_43b592ed_1532279.jpeg "api产品架构图.jpg")


# PART2 原型

## 交互及界面设计

## 信息设计

## 原型文档

## 口头操作说明


# PART3 API产品使用关键AI或机器学习之API的输出入展示

## API使用水平 
- 百度AI动物识别API
    - 西伯利亚虎精确度：57%
![输入图片说明](https://images.gitee.com/uploads/images/2019/1204/101251_c4b09712_1532279.png "屏幕快照 2019-12-04 10.08.21.png")

- [获取access_token示例代码](https://ai.baidu.com/docs#/Auth/top)
```
# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
response = requests.get(host)
if response:
    print(response.json())
```
- 调用百度AI动物识别的API代码

```

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

""" 调用动物识别 """
client.animalDetect(image);

""" 如果有可选参数 """
options = {}
options["top_num"] = 3
options["baike_num"] = 5

""" 带参数调用动物识别 """
client.animalDetect(image, options)


```




## API使用比较分析


- 动物识别：
    - 阿里云动物识别：
    - 百度智能云：

|        | 百度AI动物识别API | 阿里云动物识别API |     |     |
| ------ | ----------------- | ----------------- | --- | --- |
| 准确度 |                   |                   |     |     |
| 价格   |                   |                   |     |     |


## API使用后风险报告

## API加分项 


## 使用到的API
- 百度AI语音技术
    - [语音合成](https://ai.baidu.com/tech/speech/tts)
        - [技术文档](https://ai.baidu.com/docs#/TTS-Online-Python-SDK/top)
    - [语音识别](https://ai.baidu.com/tech/speech)
        - [技术文档](https://ai.baidu.com/docs#/ASR-Online-Python-SDK/top)
- 百度AI图像技术
    - [动物识别](https://ai.baidu.com/tech/imagerecognition/animal)
        - [技术文档](https://ai.baidu.com/docs#/ImageClassify-Python-SDK/b47b02f1)
    - [植物识别](https://ai.baidu.com/tech/imagerecognition/plant)
        - [技术文档](https://ai.baidu.com/docs#/ImageClassify-Python-SDK/714d418f)
