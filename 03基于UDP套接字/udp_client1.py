# coding:utf-8
"""

"""

# from socket import *
import socket

ip_port = ('127.0.0.1',8889)
buffersize = 1024

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	string = input('>>>')
	#客户端发消息
	udp_client.sendto(string.encode('utf-8'), ip_port)
	# 客户端发消息需要把消息和地址封装成了一个数据报，头部是地址，服务端接收到消息，直接识别头部就知道谁发来的，
	# 然后就发消息回去就用客户端发来的头部。因为很容易区分消息来源，所以UDP不需要建立连接。
	
	#客户端收消息
	msg,server_ip_port = udp_client.recvfrom(buffersize)
	print('接收到服务器{}的消息:'.format(server_ip_port), msg.decode('utf-8'))

