from xmlrpc.server import SimpleXMLRPCServer
import sys,os 
def f1():
	return 'hello RPC'
def run(): 
	server = SimpleXMLRPCServer(('127.0.0.1', 8000), allow_none = True)
	print('127.0.0.1:8000')
	server.register_function(f1,'f1') 
	server.serve_forever()

run()

# import xmlrpc.client
# proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
# today = proxy.f1()
