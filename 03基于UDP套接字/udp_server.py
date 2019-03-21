# coding:utf-8
"""
实现udp循环接收消息
"""

# from socket import *
import socket

ip = '127.0.0.1'
port = 8889
buffersize = 1024

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM 数据报式的套接字，代表UDP
udp_server.bind((ip,port))

# 此处不需要listen和accept，因为UDP协议没有三次握手和四次挥手
print('UDP服务端启动...')
while True:
	#接收客户端消息
	msg,client_ip_port = udp_server.recvfrom(buffersize) #接收消息，客户端发消息的时候有这些东西，服务端收到的也有这些东西。
	print('接收到客户端{}的消息:'.format(client_ip_port), msg.decode('utf-8'))

	# 给客户端回消息
	udp_server.sendto('hello client'.encode('utf-8'), client_ip_port)

