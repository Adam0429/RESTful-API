# RESTful-API

只是对restful API的一个了解，
todo/api/v1.0/member ：获取本宿舍所有人的名字
todo/api/v1.0/member/(name) ：获取本宿舍其中一个人的信息
# REST的六个特性：

    Client-Server：服务器端与客户端分离。
    Stateless（无状态）：每次客户端请求必需包含完整的信息，换句话说，每一次请求都是独立的。
    Cacheable（可缓存）：服务器端必需指定哪些请求是可以缓存的。
    Layered System（分层结构）：服务器端与客户端通讯必需标准化，服务器的变更并不会影响客户端。
    Uniform Interface（统一接口）：客户端与服务器端的通讯方法必需是统一的。
    Code on demand（按需执行代码？）：服务器端可以在上下文中执行代码或者脚本？

# RESTful web service的样子

REST架构就是为了HTTP协议设计的。RESTful web services的核心概念是管理资源。资源是由URIs来表示，客户端使用HTTP当中的'POST, OPTIONS, GET, PUT, DELETE'等方法发送请求到服务器，改变相应的资源状态。

HTTP请求方法通常也十分合适去描述操作资源的动作：
HTTP方法 	动作 	例子
GET 	获取资源信息 	

http://example.com/api/orders

（检索订单清单）
GET 	获取资源信息 	

http://example.com/api/orders/123

（检索订单 #123）
POST 	创建一个次的资源 	

http://example.com/api/orders

（使用带数据的请求，创建一个新的订单）
PUT 	更新一个资源 	

http://example.com/api/orders/123

（使用带数据的请求，更新#123订单）
DELETE 	删除一个资源 	

http://example.com/api/orders/123

删除订单#123

REST请求并不需要特定的数据格式，通常使用JSON作为请求体，或者URL的查询参数的一部份。


# 综述

综合上面的解释，我们总结一下什么是RESTful架构：

　　（1）每一个URI代表一种资源；

　　（2）客户端和服务器之间，传递这种资源的某种表现层；

　　（3）客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。
