#coding:utf-8
"""
"""
from socket import *

ip = '127.0.0.1'
port = 8888
backlog = 5 
buffersize = 1024 

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server.bind((ip,port)) 
tcp_server.listen(backlog)
print('服务端在等待连接...')
conn,c_addr = tcp_server.accept()
print('接收到{}的连接请求对象：{}==>'.format(c_addr,conn))

from_c_data1 = conn.recv(buffersize) #第一次客户端发来消息，睡了几秒，不会导致粘包现象
print(from_c_data1)

from_c_data2 = conn.recv(buffersize) #第二次客户端和第三次的间隔较短，产生粘包现象
print(from_c_data2)

from_c_data3 = conn.recv(buffersize) #第三次接收为空了，是因为客户端断开tcp连接了。
print(from_c_data3)

from_c_data4 = conn.recv(buffersize)
print(from_c_data4)

conn.close()
tcp_server.close()

