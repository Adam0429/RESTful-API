from kazoo.client import KazooClient  
import time  
zk = KazooClient(hosts='localhost:2181',timeout=1)
zk.start(timeout=2)  

  
if __name__ == '__main__':  
    # zk.delete('/kwsy') 
    # print(zk.get('/mysql/host',watch=mysql_watcher2))
    # print(zk.get('/mysql/port',watch=None))
    # print(zk.get('/mysql/user',watch=None))
    # print(zk.get('/mysql/pwd',watch=None))
    zk.create('/todo/api/v1.0/member') 
    zk.stop()  
