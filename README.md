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
数据创建名称叫mariadb。 
跑http。

docker run -d -p 5000:5000 --name py-http --link mariadb:mysql demo/py-http:1.0
1
特别注意这里的–link 容器名:昵称，然后对于py-http容器来说mysql就是昵称了。 
可以直接看下evn环境：

# docker exec -it py-http bash
bash-4.3# env
HOSTNAME=db7f7aba7c2f
MYSQL_ENV_MYSQL_ROOT_PASSWORD=root
MYSQL_ENV_MARIADB_VERSION=10.1.19+maria-1~jessie
MYSQL_ENV_GOSU_VERSION=1.7
MYSQL_PORT_3306_TCP_PORT=3306
MYSQL_ENV_MARIADB_MAJOR=10.1
MYSQL_PORT_3306_TCP=tcp://172.17.0.2:3306
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/
TZ=Asia/Shanghai
SHLVL=1
HOME=/root
MYSQL_NAME=/py-http/mysql
MYSQL_PORT_3306_TCP_PROTO=tcp
MYSQL_PORT_3306_TCP_ADDR=172.17.0.2
MYSQL_PORT=tcp://172.17.0.2:3306
_=/usr/bin/env
 


可以看到，在py-http容器下面已经把mariadb容器的环境变量直接引入了。 
并且查看hosts:

# cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.2      mysql 48bd5fbf3ddc mariadb
172.17.0.3      db7f7aba7c2f

可以看到有了mysql变量的host了。 
在外部访问：就说明测试成功。数据库能插入查询了。

# curl http://127.0.0.1:5000/add
ok[root@localhost http]# curl http://127.0.0.1:5000/list
results:
id:1,name:zhangsan
id:2,name:zhangsan