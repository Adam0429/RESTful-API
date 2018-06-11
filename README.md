前后端·html+flask+python
前端主要实现了添加，查询和打印数据库三个功能，在主界面中可以直接看到数据库中的信息，
在/search中可以查找，找不到会返回No result,在/add中可以添加新的blog.

add_blog,get_blog写在了service中，service是单例模式，方便管理

微服务:
/todo/api/v1.0/add/blog/
/todo/api/v1.0/search/blog/
/todo/api/v1.0/search/blogs/

RPC实现使用python第三方库xmlprc,app/web2.py 模拟了rpc服务器的建立,web.py的方法模拟了rpc调用远程客户端的方式.在项目中rpc技术用来实现统一数据

docker镜像文件路径docker/Dockerfile

zookeeper 中的conf文件夹有zoo.cfg文件 其中有datadir 和logdir 分别为数据输出和日志, 首次运行用户需要执行 echo serverid >> filelocation
zoo.cfg文件中有三个ip分别为三台服务器的ip地址
python 中应用到znode文件用于新建节点监听其他节点或者存储数据,fAILURE.PY 为检测节点失败的文件, lock.py 为避免数据冲突


