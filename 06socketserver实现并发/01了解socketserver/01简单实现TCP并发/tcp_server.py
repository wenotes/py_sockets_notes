#coding:utf-8
"""
初级了解
"""
import socketserver

class MyRequest(socketserver.BaseRequestHandler):
	def handle(self): #这个方法必须定义，在BaseRequestHandler基类里面有说明
		print('conn :',self.request)
		print('addr :',self.client_address)
		while True: #通信循环
			try:
				msg = self.request.recv(1024)
				if not msg:
					print('等待新的连接..')
					break

				print('收到客户端{}的信息：{}'.format(self.client_address, msg.decode('utf-8')))
				self.request.send('我已收到你的信息'.encode('utf-8'))
			except Exception as e:
				print(e,'等待新的连接...')
				break

if __name__ == '__main__':
	ip_port = ('127.0.0.1',8888)
	ss = socketserver.ThreadingTCPServer(ip_port, MyRequest) #多线程
	# ss = socketserver.ForkingTCPServer(ip_port, MyRequest) #多进程，多线程计算机资源开销高，Windows实验这行不行
	print('TCP服务端已启动...')

	ss.serve_forever()
