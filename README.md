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
  
  
  并给相应的访问返回json数据  在1.PY 文件中访问本地的2182端口并加监听器,监听器有三个状态用于观察状态
Zookeeper 的核心是原子广播，这个机制保证了各个Server之间的同步。实现这个机制的协议叫做Zab协议。Zab协议有两种模式，它们分别是恢复模式（选主）和广播模式（同步）。当服务启动或者在领导者崩溃后，Zab就进入了恢复模式，当领导者被选举出来，且大多数Server完成了和 leader的状态同步以后，恢复模式就结束了。状态同步保证了leader和Server具有相同的系统状态
无论连接到哪个服务器都会显示一个页面
LOOKING：当前Server不知道leader是谁，正在搜寻
LEADING：当前Server即为选举出来的leader
FOLLOWING：leader已经选举出来，当前Server与之同步
zookeeper 是一种集中管理数据的方法，用于确保一致性和稳定性
1.	py 创建了两个节点，并创建子节点去观察父节点
znode 可以实现存储数据


###Docker

Dockerfile用来创建一个自定义的image,包含了用户指定的软件依赖等。当前目录下包含Dockerfile,使用命令build来创建新的image,并命名为edwardsbean/centos6-jdk1.7:

如何编写一个Dockerfile,格式如下：

# CommentINSTRUCTION arguments
FROM


基于哪个镜像

RUN


安装软件用

MAINTAINER


镜像创建者

CMD


container启动时执行的命令，但是一个Dockerfile中只能有一条CMD命令，多条则只执行最后一条CMD.


CMD主要用于container时启动指定的服务，当docker run command的命令匹配到CMD command时，会替换CMD执行的命令。如:
Dockerfile:

CMD echo hello world

运行一下试试:

edwardsbean@ed-pc:~/software/docker-image/centos-add-test$ docker run centos-cmd
hello world

一旦命令匹配：

edwardsbean@ed-pc:~/software/docker-image/centos-add-test$ docker run centos-cmd echo hello edwardsbean
hello edwardsbean
ENTRYPOINT


container启动时执行的命令，但是一个Dockerfile中只能有一条ENTRYPOINT命令，如果多条，则只执行最后一条


ENTRYPOINT没有CMD的可替换特性

USER


使用哪个用户跑container

如：

ENTRYPOINT ["memcached"]
USER daemon
EXPOSE


container内部服务开启的端口。主机上要用还得在启动container时，做host-container的端口映射：

docker run -d -p 127.0.0.1:33301:22 centos6-ssh

container ssh服务的22端口被映射到主机的33301端口 

Fig

Fig 主要用来跟 Docker 一起来构建基于 Docker 的复杂应用，Fig 通过一个配置文件来管理多个Docker容器，非常适合组合使用多个容器进行开发的场景。目前Fig已经升级并更名为Compose。