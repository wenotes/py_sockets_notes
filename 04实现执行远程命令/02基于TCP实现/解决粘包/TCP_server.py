#coding:utf-8
"""

"""
from socket import *
import subprocess
import struct

ip = '127.0.0.1'
port = 8888
backlog = 5 
buffersize = 1024 

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server.bind((ip,port)) 
tcp_server.listen(backlog)

while True:
	print('服务端在等待连接...')
	conn,c_addr = tcp_server.accept()
	print('接收到{}的连接请求对象：{}==>'.format(c_addr,conn))

	while True:
		try:
			cmd = conn.recv(buffersize) 
			if not cmd:
				print('服务端接收消息为空，断开当前连接!')
				break 
		except ConnectionResetError as e: 
			print(e)
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
				res_cmd = b'success!' #暂时这样
		# low版解决粘包，先求res_cmd的字节长度，先传给客户端，然后客户端的buffersize改成那个就好了。如果服务端返回的字节超过你本机的极限buffersize，客户端一次recv根本收不了，那就有问题了，这样也可以解决，客户端循环recv把消息全部接受完就可以了。
		# 弊端：先发编码后的数据长度给客户端，由于客户端不知道数据长度的字节长度，得给服务端回一个我知道你字节长度大小的消息，服务端知道客户端知道数据长度后才能发真正的数据。
		
		# 高级一点的方法，利用struct模块，通过pack方法将数据长度（此处指的是int类型，具体其他类型百度）统一变为固定4个字节的东西，然后客户端unpack这四个字节就可以知道真正的数据长度了。
		length = len(res_cmd)
		s_p = struct.pack('i',length) #i代表int类型，这样就可以将数据长度以4个字节的形式先传给客户端

		conn.send(s_p)
		
		conn.send(res_cmd)

	conn.close()
tcp_server.close()

