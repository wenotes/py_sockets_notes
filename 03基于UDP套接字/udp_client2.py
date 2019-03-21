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
	#客户端发消息需要带上地址和端口，因为你看看TCP客户端在发消息之前也connect了，这是udp的方式。
	
	#客户端收消息
	msg,server_ip_port = udp_client.recvfrom(buffersize)
	print('接收到服务器{}的消息:'.format(server_ip_port), msg.decode('utf-8'))

