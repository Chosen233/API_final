# 项目名称：学前班
# Product Requirement（产品说明文档）

| Title                     | Content |
| ------------------------- | ------- |
| Target release(发布日期)  | 2019/11 |
| Epic(史诗名称)            | 学前班 |
| Document status(文档状态) | 进行中  |
| Document owner(文件主人)  | 潘卓祺  |
| Designer(领头的设计师)    | 潘卓祺  |
| Developer(领头的开发者)   | 潘卓祺  |
| QA(领头的测试者)          | 潘卓祺  |

# Catalogue（目录）
- [Part1 PRD价值主张设计](#价值主张设计)
    - [PRD1加值宣言](#加值宣言)
    - [PRD2核心价值](#核心价值)
    - [PRD3核心价值与用户痛点](#核心价值与用户痛点)
    - [PRD4人工智能概率性与用户痛点](#人工智能概率性与用户痛点)
    - [PRD5需求列表与人工智能API加值](#需求列表与人工智能API加值)
- [Part2 原型](#原型)
    - [交互及界面设计](#交互及界面设计)
    - [信息设计](#信息设计)
    - [原型文档](#原型文档)
    - [口头操作说明](#口头操作说明)
- [Part3 API产品使用关键AI或机器学习之API的输出入展示](#API产品使用关键AI或机器学习之API的输出入展示)
    - [API使用水平](#使用水平)
    - [API使用比较分析](#使用比较分析)
    - [API使用后风险报告](#使用后风险报告)
    - [API加分项](#加分项)

## 产品定位
“学前班”帮助3到8岁的幼年儿童为开学做好准备而设计的科普类互动学习应用软件。皆在为培养3-8岁幼年儿童的认知能力、责任感和耐心等。


## 背景
- 3-8岁的幼年儿童正处于思维发展的关键时候的时候，对外界的一切因素都感到非常的好奇。美国著名心理学家[本杰明·布鲁姆Benjamin Bloom](https://baike.baidu.com/item/%E5%B8%83%E9%B2%81%E5%A7%86/19755801)的研究认为，**若人在17岁所达到的智力水平为100%，那么儿童在4岁时已具备了其中的50%，4～8岁期间获得30%，而8～17岁这一阶段只增加了20%。** 可以看出，孩子的脑发展（智力发展），关键的节点出现在8岁之前。
![智力](https://images.gitee.com/uploads/images/2019/1204/142736_300a5930_1532279.png "屏幕快照 2019-12-04 14.27.20.png")

- 有时候家长因为不了解／不知道／缺乏经验而不能解决幼年儿童的问题（如：这是什么动物、这是什么植物、这是什么垃圾等），减轻家长教育孩子的负担。

- 通过对一系列的识别类APP调查，几乎所有的识别类APP与科普类APP的目标用户都偏向大龄儿童以上，没有一款是针对幼年儿童设计的APP。同时科普类APP不支持拍照识别的功能。目前市场上有几个下载量比较大的识别动植物／科普类的APP：
    - “动物识别器APP”：只能通过拍照识别动物，不能通过文字搜索动物。点开了解动物详情后，页面跳转到百度百科。对于幼年儿童来说，年龄较低的儿童，识字能力有限，所以不能很好的阅读完全部内容。
    - “全能识别王APP”：百度AI上的图像识别功能几乎都用上了，也是只能通过拍照识别，不支持文字搜索。
    - “科普中国APP”：目标用户为各年龄阶层。科普的内容为天文地理，知识过于广泛，幼年儿童在理解上有一定的困难。


## 目标

- 通过使用百度AI（植物识别、动物识别、通用物体识别）的功能，让幼年儿童在外游玩的时候能过通过本产品进行科普学习。
- 在室内的时候，又能通过本产品的游戏对学习的内容进行二次回顾。
    
**游戏互动：**
- 动物影子游戏：使用动物识别API，将识别过的动物汇集到一起，弄成一个动物影子游戏，提高幼年儿童的认知能力。    
- 画画游戏：使用植物／动物识别API，将识别过的植物／动物汇集到一起，弄成一个植物／动物绘本游戏，提高幼年儿童的认知能力与书写技能。
- 回收游戏：使用通用物体识别API，学习对各种类型的垃圾进行分类和回收并培养责任感。


# 价值主张设计

## 加值宣言

本产品皆在通过使用人工智能的部分功能（图像识别）来实现更好的科普效果，培养3-8岁幼年儿童的认知能力、责任感和耐心等。

- （主要）百度AI的动物识别API对本产品价值部分在于：识别近八千种动物，接口返回动物名称，并获取百科信息，适用于拍照识图类APP中。
   
- （主要）百度AI的植物识别API对本产品价值部分在于：支持识别超过2万种通用植物和近8千种花卉，接口返回植物的名称，并获取百科信息，适用于拍照识图类APP中。
 
- （主要）图像通用物体和场景识别：支持超过10万类常见物体和场景识别，接口返回图片内1个或多个物体的名称，并可获取百科信息。适用于图像或视频内容分析、拍照识图等业务场景。


## 核心价值
- 动物识别：最小可用产品为拍照／上传动物的图片，返回该动物的名称、详细信息及可信度。
- 植物识别：最小可用产品为拍照／上传植物的图片，返回该植物的名称、详细信息及可信度。
- 图像通用物体和场景识别：最小可用产品为拍照／上传动物的图片，返回该物品的名称、详细信息。

## 核心价值与用户痛点
- 在外活动的时候，家长想教育孩子一些知识时偶尔会遇到无法回答的问题，无法给孩子进行详细的说明。
- 家长想用更加有趣的方式给孩子进行科普，而不想用枯燥的传统方式给孩子进行教育。
- 找不到一款适合幼年儿童使用的科普类app。
- （该功能考虑中）在幼年儿童单独使用的时候，会遇到不认识的字。


## 人工智能概率性与用户痛点
- 照片清晰度较好的时候
- 照片模糊，同类型不同品种的动物／植物识别成功率较低，对于在移动中的用户来说不太友好。
- 用户拍摄的照片中植物品种数量多，识别结果的准确度十分低。

    - 西伯利亚虎原图
    ![动物识别](https://images.gitee.com/uploads/images/2019/1203/204953_342b473c_1532279.png "屏幕快照 2019-12-03 20.49.27.png")
    
    - 模糊后
    ![模糊后](https://images.gitee.com/uploads/images/2019/1203/205627_4bfb5eee_1532279.png "屏幕快照 2019-12-03 20.55.57.png")
    

## 需求列表与人工智能API加值

需求列表

| #   | User Story（用户案例）                                                                                         | Importance（重要性） | Notes（笔记） | 技术         |
| --- | -------------------------------------------------------------------------------------------------------------- | -------------------- | ------------- | ------------ |
| 1   | 李女士带小明在外游玩，小明问李女士这是什植物，李女士不清楚，无法回答小明的问题                                 | 极其重要             | 核心功能      | 植物识别     |
| 2   | 李女士带小明在外游玩，小明问李女士这是什动物，李女士不清楚，无法回答小明的问题                                 | 极其重要             | 核心功能      | 动物识别     |
| 3   | 李女士和小明一起参加儿童环保志愿活动，李女士和小明手上拿到了玻璃垃圾，不知道玻璃属于可回收垃圾还是不可回收垃圾 | 极其重要重要         | 核心功能      | 通用物体识别 |


## 产品架构图
![产品架构图](https://images.gitee.com/uploads/images/2019/1203/233301_43b592ed_1532279.jpeg "api产品架构图.jpg")


# PART2 原型

## 交互及界面设计

## 信息设计

## 原型文档

## 口头操作说明


# PART3 API产品使用关键AI或机器学习之API的输出入展示

## 使用水平 
- [百度AI动物识别API](https://ai.baidu.com/docs#/ImageClassify-Python-SDK/b47b02f1)
    - 西伯利亚虎准确度：57%
![输入图片说明](https://images.gitee.com/uploads/images/2019/1204/101251_c4b09712_1532279.png "屏幕快照 2019-12-04 10.08.21.png")

- [百度AI植物识别API](https://ai.baidu.com/docs#/ImageClassify-Python-SDK/714d418f)
    - 大叶金顶杜鹃准确度：80%
![输入图片说明](https://images.gitee.com/uploads/images/2019/1204/103926_c3efc0dd_1532279.png "屏幕快照 2019-12-04 10.37.56.png")

- 百度语音合成API

- 百度语音识别API


## 使用比较分析

- 动物识别：
    - [腾讯云图像分析](https://cloud.tencent.com/act/event/tiiademo)
![输入图片说明](https://images.gitee.com/uploads/images/2019/1204/114540_35809baf_1532279.png "屏幕快照 2019-12-04 11.44.20.png")

    - 百度智能云：

|        | 百度AI动物识别API | 阿里云动物识别API |     |     |
| ------ | ----------------- | ----------------- | --- | --- |
| 准确度 |                   |                   |     |     |
| 价格   |                   |                   |     |     |


## 使用后风险报告

## 加分项 


## 使用到的API

- 百度AI图像技术
    - [动物识别](https://ai.baidu.com/tech/imagerecognition/animal)
        - [技术文档](https://ai.baidu.com/docs#/ImageClassify-Python-SDK/b47b02f1)
    - [植物识别](https://ai.baidu.com/tech/imagerecognition/plant)
        - [技术文档](https://ai.baidu.com/docs#/ImageClassify-Python-SDK/714d418f)
    - [通用物体识别](https://ai.baidu.com/tech/imagerecognition/general)
        - [技术文档](https://ai.baidu.com/docs#/ImageClassify-Python-SDK/0358318c)
