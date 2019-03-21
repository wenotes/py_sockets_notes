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

	s_p = tcp_client.recv(4) #先接受到服务端传过来的4个字节

	length= struct.unpack('i',s_p)[0] #unpack这四个字节，返回一个元组形式的东西，第一个值是int类型的真正数据长度，第二个丢弃
	# low版：然后下面通过length循环接收数据
	all_res = b''
	recved_size = 0
	while length>recved_size: #如果数据长度超过buffersize，进入循环
		res = tcp_client.recv(buffersize)
		all_res += res 
		recved_size = len(all_res)

	# 通过迭代器iter和偏函数partial，接收数据
	# all_res = ''.join(iter(partial(tcp_client.recv, buffersize), b'')) #装逼没成功待解决
	print('服务端返回的命令执行结果↓↓\n', all_res.decode('gbk'))

tcp_client.close()

