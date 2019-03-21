#coding:utf-8
"""
"""
from socket import *

ip = '127.0.0.1'
port = 8888
backlog = 5 
buffersize = 12

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server.bind((ip,port)) 
tcp_server.listen(backlog)
print('服务端在等待连接...')
conn,c_addr = tcp_server.accept()
print('接收到{}的连接请求对象：{}==>'.format(c_addr,conn))

from_c_data1 = conn.recv(buffersize) #
print(from_c_data1)

from_c_data2 = conn.recv(buffersize) #
print(from_c_data2)

from_c_data3 = conn.recv(buffersize) 
print(from_c_data3)

from_c_data4 = conn.recv(buffersize)
print(from_c_data4)

conn.close()
tcp_server.close()

