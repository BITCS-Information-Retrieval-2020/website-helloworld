# website-helloworld

## 基于 Vue + Element-UI + Django 的论文综合搜索项目

# 目录

- [项目启动流程](##环境要求)
  - [环境要求](#环境要求)
  - [部署过程](#部署过程)
  - [运行项目](#运行项目)
- [前端目录结构](#前端目录结构)
- [后端目录结构](#后端目录结构)
- [项目功能展示](#项目功能展示)
- [前后端接口说明](#前后端接口说明)
- [前端页面之间参数传递](#前端页面之间参数传递)
- [第三方库依赖](#第三方库依赖)
- [小组分工](#小组分工)

## 项目启动流程

### 环境要求

- NodeJS 8.12+ 环境
- python 3.0+

### 部署过程

1. 前端
```bash
前端 Vue + ElementUI
#1. 需要安装nodejs （安装完成后会自动安装npm）直接到nodejs官网下载安装即可
#2. 
cd 到文件目录 在该目录下安装依赖
#3. install dependencies
npm install
#4. serve with hot reload at localhost:8080
npm run dev
```
2. 后端 Django
```bash
#1. 需要安装python
#2. 安装 djano 
sudo pip3 install Django -i https://pypi.tuna.tsinghua.edu.cn/simple
#3. cd到后端项目文件目录下
cd testdj # 
#4. 安装检索pip包
pip install search_utils-1.0.0.tar.gz
```

### 运行项目

~~~shell
$ npm run dev # 开发环境下运行
$ npm run build # 打包编译发布
$ python manage.py runserve # 启动 django
~~~

## 前端目录结构

~~~bash
├─ config 			// 项目配置 webpack
├─ static
|  ├─ images 		// 存放所有图片资源
├─ src
│  ├─ components  	// 存放所有组件 component
│  │  ├─ AdvancedSearch.vue  	// 高级检索组件
│  │  ├─ CopyRight.vue  	// 版权信息组件
│  │  ├─ Index.vue 	// 检索首页
│  │  ├─ LocalHeader.vue  	// 首页头部组件
│  │  ├─ PageInfor.vue  	// 论文详情组件
│  │  ├─ SearchPage.vue  	// 检索结果展示页
│  │  ├─ SearchWindows.vue  	// 普通检索组件
│  ├─ router      	// 项目路由导航 router
│  ├─ store      	// 项目状态管理 store
│  ├─ App.vue   	// 入口文件
│  └─ main.js   	// 插件声明
~~~

## 后端目录结构

~~~bash
├─ LiteratureSearch		// 应用	
|  ├─ _init_py 			
|  ├─ admin.py		//  配置模型models在django原生后台的管理
|  ├─ app.py		// 应用级别的配置
|  ├─ search_utils.py		// 检索代码
|  ├─ urls.py		// 路由设置
|  ├─ views.py		// 控制层
|  ├─ model.py		// 模型定义
├─ MydjangoProject
│  ├─ _init_py  	
│  ├─ asgi.py  	
│  ├─ settings.py 	// 项目配置
│  ├─ urls.py  	// 项目路由定义
│  ├─ wsgi.py  	// nginx/apache
├─ templates      	
├─ manage.py      	

~~~

## 项目功能展示

系统总共由三个部分组成，分别为1.检索首页 2.检索结果页 3.论文详情页

1. ### 检索首页

   (1) 普通检索
   a)	不设置检索自段默认全文检索
   b)	可按照标题、作者、摘要字段指定一个进行搜索
   c)	用户在搜索框输入文字时，可以实时提示补全信息。
   d)	按钮能够跳转到高级检索界面实现能够指定多个字段进行搜索
   e)	检查输入是否合法

   ![首页检索](https://github.com/BITCS-Information-Retrieval-2020/website-helloworld/blob/master/FNSearch-master/img/%E9%A6%96%E9%A1%B5%E6%A3%80%E7%B4%A2.PNG)

   (2) 高级检索
   a) 高级检索支持与或非三种逻辑 
   b) 支持时间范围选择
   c) 只支持author和title两者之间的逻辑
   d) 检查输入是否合法

   ![高级检索](https://github.com/BITCS-Information-Retrieval-2020/website-helloworld/blob/master/FNSearch-master/img/%E9%AB%98%E7%BA%A7%E6%A3%80%E7%B4%A2.png)

2. ### 检索结果展示页

   a)	首先显示总共检索到了多少条数据以及检索所用的时间
   b)	每一条展示论文的标题、作者、摘要、年份简要信息
   c)	上方导航条可以返回首页也可以重新检索
   d)	可按照相关度或者年份进行结果排序(默认为相关度排序)
   e)	根据后台是否有PDF、视频、数据链接动态展示
   f)        展示pdf缩略图(由于没有爬取处理，这里是写死的)

   ![img\检索结果.png](https://github.com/BITCS-Information-Retrieval-2020/website-helloworld/blob/master/FNSearch-master/img/%E6%A3%80%E7%B4%A2%E7%BB%93%E6%9E%9C.png)

3. ### 论文详情页

   a)	上方同样展示导航条 能够返回首页和搜索
   b)	展示标题 作者 论文的唯一标志、出版社、DOI 
   c)	根据后台返回数据是否为空动态展示：摘要、视频、PDF链接、数据集链接；
   d)      如果后台返回有视频链接，可直接播放(仅支持存储到后台的视频 不支持在线视频)

	![论文详情1](https://github.com/BITCS-Information-Retrieval-2020/website-helloworld/blob/master/FNSearch-master/img/%E8%AE%BA%E6%96%87%E8%AF%A6%E6%83%851.png)

	![论文详情2](FNSearch-master\img\论文详情2.pnghttps://github.com/BITCS-Information-Retrieval-2020/website-helloworld/blob/master/FNSearch-master/img/%E8%AE%BA%E6%96%87%E8%AF%A6%E6%83%852.PNG)



## 前后端接口说明

### 1.输入关键字提示

| 接口详情 |                           |
| -------- | ------------------------- |
| 地址     | `localhost:8000/suggest`/ |
| 请求方式 | `GET`                     |

#### url示例

localhost:8000/suggest/?keyword="li"

------

#### 请求参数

| 字段    | 说明         | 类型     | 备注 | 是否必填 |
| ------- | ------------ | -------- | ---- | -------- |
| keyword | `搜索关键字` | `string` |      | `是`     |

------

#### 建议响应示例

```
[{
    value: "Audrey Acken article"
},
{
    value: "Audrey Acken"
}]
```

### 2.搜索接口

| 接口详情 |                        |
| -------- | ---------------------- |
| 地址     | localhost:8000/search/ |
| 请求方式 | `GET`                  |

------

#### url示例

localhost:8000/search/?query=1&theme="author"&page=1&order=1&year="1980,2020"

------

#### 请求参数

| 字段  | 说明         | 类型     | 备注 | 是否必填 |
| ----- | ------------ | -------- | ---- | -------- |
| query | `搜索关键字` | `string` |      | `是`     |
| theme | `搜索主题`   | `string` |      | `否`     |
| page  | `页码`       | `string` |      | `否`     |
| order | `排序`       | `string` |      | `否`     |
| year  | `检索年份`   | `string` |      | `否`     |

高级检索:theme=author,abstract,title 用英文逗号隔开

现支持字段:author,adbtract,title(作者,摘要,标题,空的话为全支持) order为1 支持时间正序，order为2 支持时间倒序，其他情况或者为空都为相关度排序

year为检索年份：如用英文逗号隔开，标识年份范围（1997,2008），单一年份直接写即可

------
#### 检索响应示例
```
{
  "code": 1, 
  "data": [
    {
      "abstract": "With the COVID-19 pandemic raging world-wide since the beginning of the 2020 decade, the need for monitoring systems to track relevant information on social media is vitally important. This paper describes our submission to the WNUT-2020 Task 2: Identification of informative COVID-19 English Tweets. We investigate the effectiveness for a variety of classification models, and found that domain-specific pre-trained BERT models lead to the best performance. On top of this, we attempt a variety of ensembling strategies, but these attempts did not lead to further improvements. Our final best model, the standalone CT-BERT model, proved to be highly competitive, leading to a shared first place in the shared task. Our results emphasize the importance of domain and task-related pre-training.", 
      "author": "Lilei,Hanmeimei", 
      "dataset_url": "http://39.96.43.48/static/dadataset/W18-0516.Datasets.zip", 
      "keyword_in_video_time": "00:2:58", 
      "pdf": "http://39.96.43.48/static/pdf/2020.wnut-1.47.pdf", 
      "publish_month": "June", 
      "publish_year": "2018", 
      "publusher": "Association for Computational Linguistics", 
      "titile": "Pace English", 
      "video": "http://39.96.43.48/static/video/123.mp4"
    }, 
  "total": 1
  ]
}
```
#### 返回字段说明：

| 返回字段              | 说明       |
| :-------------------- | ---------- |
| abstract              | 摘要       |
| author                | 作者       |
| dataset_url           | 数据集地址 |
| keyword_in_video_time | 视频关键字 |
| pdf                   | pdf链接    |
| publish_at            | 发布时间   |
| publisher             | 出版商     |
| video                 | 视频链接   |

------
## 前端页面之间参数定义

```
1.首页->搜索展示
(1)普通检索
传递参数为 
theme = "author" or "title" or "abstruct"
keyword = "检索框内容"
(高级检索)
query=dic({
    'author':"作者",
    'title':"标题",
    'logic':"and" or "or" or "not",
    'date':"起始年份,结束年份"(用，隔开)
})


2.结果展示页->论文详情页
info = dic({
    'abstract': "摘要",
    'author': "作者",
    'dataset_url': "数据集",
    'keyword_in_video_time': "视频关键字",
    'pdf': "pdf链接",
    'publish_at': "出版时间",
    'publisher': "出版商",
    'title': "论文标题",
    'video': "视频地址"
})

```


## 第三方库依赖

|                            依赖库                            |                             版本                             |                             文档                             |                             介绍                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|           [axios](https://github.com/axios/axios)            | [![npm version](https://img.shields.io/badge/npm-v0.18.0-orange)](https://www.npmjs.org/package/axios) |     [axios docs(zh-CN)](http://axios-js.com/zh-cn/docs/)     |                   基于 promise 的 HTTP 库                    |
|     [vue-axios](https://github.com/imcvampire/vue-axios)     | [![npm version](https://img.shields.io/badge/npm-v2.1.4-orange)](https://www.npmjs.com/package/vue-axios) | [vue-axios docs(zh-CN)](http://www.axios-js.com/zh-cn/docs/vue-axios.html) |               基于 Vue.js 和 axois 的轻度封装                |
|     [element-ui](https://github.com/ElemeFE/element.git)     | [![npm version](https://img.shields.io/badge/npm-v2.7.2-orange)](https://www.npmjs.com/package/element-ui) | [element-ui docs(zh-CN)](https://element.eleme.cn/#/zh-CN/component/installation) |                基于 Vue 2.0 开发的开源组件库                 |
|       [video.js](https://github.com/videojs/video.js)        | [![npm version](https://img.shields.io/badge/npm-v7.10.2-orange)](https://www.npmjs.com/package/video.js) |      [vedio.js docs(en-US)](https://docs.videojs.com/#)      |                  基于HTML5的网络视频播放器                   |
|      [vue-router](https://github.com/vuejs/vue-router)       | [![npm version](https://img.shields.io/badge/npm-v3.0.1-orange)](https://www.npmjs.com/package/vue-router) | [vue-router docs(zh-CN)](https://router.vuejs.org/zh/installation.html) |                     Vue 官方的路由管理器                     |
| [vue-video-player](https://github.com/surmon-china/vue-video-player) | [![npm version](https://img.shields.io/badge/npm-v5.0.2-orange)](https://www.npmjs.com/package/my-vue-video-player) | [vue-vedio-player dosc(en-US)](https://docs.videojs.com/tutorial-options.html) | 适用于 Vue 的 [video.js](https://github.com/videojs/video.js) 播放器组件 |
|            [vuex](https://github.com/vuejs/vuex)             | [![npm version](https://img.shields.io/badge/npm-v3.1.0-orange)]() |        [vuex docs(zh-CN)](https://vuex.vuejs.org/zh/)        |         专为 Vue.js 应用程序开发的**状态管理模式**库         |


## 小组分工 

|   姓名   |    学号    |       分工        | 职务 |
| :------: | :--------: | :---------------: | :--: |
|  郑慧娴  | 3220201026 |     检索首页      | 组员 |
|  翟钰坤  | 3120201092 |    检索展示页     | 组员 |
|  孙逸鲲  | 3120201063 |    检索展示页     | 组员 |
|  魏雅倩  | 3220200971 |    论文详情页     | 组员 |
|  罗晓青  | 3220200933 |    论文详情页     | 组员 |
|  胡英帅  | 3120201026 |       后端        | 组员 |
| 苗    壮 | 3220200938 | 后端+前端页面接口 | 组长 |














