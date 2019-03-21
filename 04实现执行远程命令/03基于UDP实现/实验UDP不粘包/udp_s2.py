#coding:utf-8
"""
数据量大测试不粘包，修改buffersize来模拟数据量大小
"""
from socket import *
import subprocess

ip = '127.0.0.1'
port = 8889
buffersize = 15

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
udp_server.bind((ip,port)) 

print('UDP服务端启动...')
# 等待收消息，udp中一个发必须要对应一个收
from_c_data1,client_ip_port = udp_server.recvfrom(buffersize) #需要在Linux平台上试，要不然会报OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，或该用户用于接收数据报的缓冲区比数据报小。
print(from_c_data1)

from_c_data2,client_ip_port = udp_server.recvfrom(buffersize)
print(from_c_data1)

from_c_data3,client_ip_port = udp_server.recvfrom(buffersize)
print(from_c_data1)

udp_server.close()

