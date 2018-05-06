from kazoo.client import KazooClient 
from kazoo.client import KazooState 
import time  
import logging
from kazoo.client import KazooClient
from kazoo.client import KazooState

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    zk=KazooClient(hosts='127.0.0.1:2182')
    zk.start()

    @zk.add_listener
    def my_listener(state):
        if state == KazooState.LOST:
            print("LOST")
        elif state == KazooState.SUSPENDED:
            print("SUSPENDED")
        else:
            print("Connected")

    zk.ensure_path("/todo/api/v1.0/member")

    # Create a node with data

    zk.create("/todo/api/v1.0/member/wy", b"")

    zk.create("/todo/api/v1.0/member/cyx", b"A")

    #Reading Data

    # Determine if a node exists

    if zk.exists("/todo/api/v1.0/member/"):

        print("/todo/api/v1.0/member/ is existed")

    @zk.ChildrenWatch("/todo/api/v1.0/member/")

    def watch_children(children):

        print("Children are now: %s" % children)


    @zk.DataWatch("/todo/api/v1.0/member/")

    def watch_node(data, stat):

        print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

    # Print the version of a node and its data

    data, stat = zk.get("/todo/api/v1.0/member/")

    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

    # List the children

    children = zk.get_children("/todo/api/v1.0/member/")

    print("There are %s children with names %s" % (len(children), children))

    #Updating Data

    zk.set("/todo/api/v1.0/member/", b"some data")

    #Deleting Nodes

    zk.delete("/todo/api/v1.0/member/")

    #Transactions

    transaction = zk.transaction()

    transaction.check('/todo/api/v1.0/member/', version=-1)

    transaction.create('/todo/api/v1.0/member/', b"B")

    results = transaction.commit()

    print ("Transaction results is %s" % results)

    zk.delete("/todo/api/v1.0/member/")

    time.sleep(2)

    zk.stop()

if __name__ == "__main__":
    main() 
    # zk.add_listener(my_listener)  
        # zk.start(timeout=2)  


      
    # zk.delete('/kwsy') 
    # print(zk.get('/mysql/host',watch=mysql_watcher2))
    # print(zk.get('/mysql/port',watch=None))
    # print(zk.get('/mysql/user',watch=None))
    # print(zk.get('/mysql/pwd',watch=None))
    
