#coding:utf-8
"""
客户端发送远程命令
"""
from socket import *

ip = '127.0.0.1'
port = 8888
buffersize = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect((ip,port))

while True:
	cmd = input('>>>').strip()
	if not cmd:
		print('请重新输入命令',end='')
		continue
	if cmd=='exit':
		break
	tcp_client.send(cmd.encode('utf-8'))

	cmd_res = tcp_client.recv(buffersize)
	print('服务端返回的命令执行结果↓↓\n', cmd_res.decode('gbk'))

tcp_client.close()

"""
粘包现象：
	首先，我们知道我们一次收消息的字节大小为1024字节。当收的消息大小超过1024字节呢？比如执行ipconfig /all命令。
当客户端收到服务端超过1024字节的消息时，这些消息暂存到客户端的内存缓冲区中，一次recv只能接收1024字节的消息，下次
recv的时候就会收到上次遗留下来的消息。这样的现象就叫粘包现象。
* tcp有粘包现象，udp没有
"""