#coding:utf-8
"""
客户端并发发送远程命令
"""
import socketserver
import subprocess
import struct

class MyRequest(socketserver.BaseRequestHandler):

	def handle(self):

		print('conn :',self.request)
		print('addr :',self.client_address)

		while True:
			try:
				cmd = self.request.recv(buffersize) 
				if not cmd:
					print('服务端接收消息为空，断开{}连接!'.format(self.client_address))
					break 
			except ConnectionResetError as e: 
				print(e,'等待新的连接...')
				break

			print('客户端发过来一个命令 ==>',cmd.decode('utf-8'))

			sp_obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
														stdout=subprocess.PIPE,
														stdin=subprocess.PIPE,
														stderr=subprocess.PIPE)
			err = sp_obj.stderr.read()
			if err:
				res_cmd = err
			else:
				res_cmd = sp_obj.stdout.read() 
				if not res_cmd:
					res_cmd = b'success!'
					
			s_p = struct.pack('i',len(res_cmd))

			self.request.send(s_p)
			
			self.request.send(res_cmd)

if __name__ == '__main__':
	ip_port = ('127.0.0.1',8888)
	buffersize = 1024
	socketserver.ThreadingTCPServer.request_queue_size = 5 #相当于backlog，其实默认值也是5
	socketserver.ThreadingTCPServer.allow_reuse_address = True #默认值是False
	# #相当于tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)这行的作用是为了防止端口为wait相关状态时，重启服务端会报错。

	ss = socketserver.ThreadingTCPServer(ip_port, MyRequest) #多线程
	
	print('TCP服务端已启动...')

	ss.serve_forever()
	