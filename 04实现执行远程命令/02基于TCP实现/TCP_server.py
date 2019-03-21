#coding:utf-8
"""

"""
from socket import *
import subprocess

ip = '127.0.0.1'
port = 8888
backlog = 5 
buffersize = 1024 

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server.bind((ip,port)) 
tcp_server.listen(backlog)

while True: #连接循环
	print('服务端在等待连接...')
	conn,c_addr = tcp_server.accept()
	print('接收到{}的连接请求对象：{}==>'.format(c_addr,conn))

	while True: #通信循环
		try:
			cmd = conn.recv(buffersize) #当客户端断开连接时，此时情况要么是报一个异常（异常终止客户端会导致服务端报异常）或者一直收空（正常close客户端会导致服务端一直收空）
			if not cmd:
				print('服务端接收消息为空，断开当前连接!')
				break #收空处理
		except ConnectionResetError as e: #异常处理
			print(e)
			break

		print('客户端发过来一个命令 ==>',cmd.decode('utf-8'))
		#服务端进行执行命令，此处利用subprocess模块
		sp_obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
													stdout=subprocess.PIPE,
													stdin=subprocess.PIPE,
													stderr=subprocess.PIPE)
		err = sp_obj.stderr.read()
		if err:
			res_cmd = err
		else:
			res_cmd = sp_obj.stdout.read() #在Windows上执行命令返回的字符串编码是gbk的，所以客户端那边解码的时候也得是gbk
			if not res_cmd:# 当命令返回值是空的话，比如cd..命令
				res_cmd = b'success!' #暂时这样
		conn.send(res_cmd)

	conn.close()
tcp_server.close()

