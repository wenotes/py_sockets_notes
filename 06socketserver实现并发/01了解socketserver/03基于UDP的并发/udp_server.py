#coding:utf-8
"""
基于udp实现并发，可能你会说UDP不是本来就是这样吗，所以说这个用的不多
"""
import socketserver

class MyRquest(socketserver.BaseRequestHandler):
	def handle(self): #这个方法必须定义，在BaseRequestHandler基类里面有说明，这里想想当于TCP连接循环，相当于UDP的通信循环
		print('msg,socket对象 :',self.request)
		print('addr :',self.client_address)

		msg = self.request[0]
		print('收到客户端{}的信息：{}'.format(self.client_address, msg.decode('utf-8')))
		
		self.request[1].sendto('我已收到你的信息'.encode('utf-8'), self.client_address)

if __name__ == '__main__':
	ip_port = ('127.0.0.1',8889)
	ss = socketserver.ThreadingUDPServer(ip_port, MyRquest) #多线程
	print('UDP服务端已启动...')

	ss.serve_forever()
