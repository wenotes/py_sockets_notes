#coding:utf-8
"""
"""
from socket import *

ip_port = ('127.0.0.1',8888)

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
	client_msg = input('>>>')
	if not client_msg: 
		print('请重新输入消息',end='')
		continue
	if client_msg=='exit':
		break

	tcp_client.send(client_msg.encode('utf-8'))

	msg = tcp_client.recv(1024)
	print('服务端返回的消息: {}'.format(msg.decode('utf-8')))

tcp_client.close()
