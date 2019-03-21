#coding:utf-8
"""
"""
from socket import *
import os, hmac

secret_key = b'rangniheiheihei'

def conn_auth(conn):
	# 跟服务端进行校检身份
	auth_bytes = conn.recv(32) #收到服务端发的一个32位的auth_bytes
	h = hmac.new(secret_key, auth_bytes)
	digest = h.digest()
	conn.send(digest)

def client_handle(ip_port, buffersize=1024):
	tcp_client = socket(AF_INET, SOCK_STREAM)
	tcp_client.connect((ip_port))
	# 通信前进行合法验证
	conn_auth(tcp_client)
	print('连接合法，可以通信...')
	while True:
		client_msg = input('>>>')
		if not client_msg: 
			print('请重新输入消息',end='')
			continue
		if client_msg=='1':
			break
		tcp_client.send(client_msg.encode('utf-8'))

		msg = tcp_client.recv(2048)
		print('服务端返回的消息: {}'.format(msg.decode('utf-8')))

	tcp_client.close()
if __name__ == '__main__':
	ip_port = ('127.0.0.1',8888)
	client_handle(ip_port)
