#coding:utf-8
"""
客户端发送远程命令
"""
from socket import *
import struct
from functools import partial

ip = '127.0.0.1'
port = 8888
buffersize = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect((ip,port))

while True:
	cmd = input('>>>').strip()
	if not cmd:
		print('请重新输入命令',end='')
		continue
	if cmd=='exit':
		break
	tcp_client.send(cmd.encode('utf-8'))

	s_p = tcp_client.recv(4) 

	length= struct.unpack('i',s_p)[0] 
	
	all_res = b''
	recved_size = 0
	while length>recved_size: 
		res = tcp_client.recv(buffersize)
		all_res += res 
		recved_size = len(all_res)

	print('服务端返回的命令执行结果↓↓\n', all_res.decode('gbk'))

tcp_client.close()

