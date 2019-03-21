#coding:utf-8
"""
模拟tcp客户端1收发消息

"""
from socket import *

ip = '127.0.0.1'
port = 8888

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect((ip,port))
# tcp_client.connect_ex((ip,port)) #connect的扩展版本，出错时返回出错码，不会抛出异常

while True:
	client_msg = input('>>>')
	if not client_msg: #防止卡住
		print('请重新输入消息',end='')
		continue
	if client_msg=='1':
		break
	tcp_client.send(client_msg.encode('utf-8'))

	msg = tcp_client.recv(2048)
	print('服务端返回的消息: {}'.format(msg.decode('utf-8')))

tcp_client.close()

"""
收发消息过程:
	输入msg ==> 客户端send msg ==> 发到自己机器上的客户端套接字缓冲区
	客户端套接字缓冲区中的消息 ==> 通过网卡发送 ==> 到服务端的套接字缓冲区中
	服务端recv msg ==> 从自己的机器的套接字缓冲区中获取消息 ==> 读取msg 

* 当套接字缓冲区中没东西，则收会卡住

"""