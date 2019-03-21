#coding:utf-8
"""
模拟tcp客户端2收发消息
"""
from socket import *

ip = '127.0.0.1'
port = 8888

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect((ip,port))

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
