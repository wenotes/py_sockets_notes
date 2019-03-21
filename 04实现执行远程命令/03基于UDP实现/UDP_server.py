#coding:utf-8
"""

"""
from socket import *
import subprocess

ip = '127.0.0.1'
port = 8889
buffersize = 1024 

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
udp_server.bind((ip,port)) 

print('UDP服务端启动...')
while True:
	# 等待收消息
	cmd,client_ip_port = udp_server.recvfrom(buffersize)

	print('客户端发过来一个命令 ==>',cmd.decode('utf-8'))
	sp_obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
												stdout=subprocess.PIPE,
												stdin=subprocess.PIPE,
												stderr=subprocess.PIPE)
	err = sp_obj.stderr.read()
	if err:
		res_cmd = err
	else:
		res_cmd = sp_obj.stdout.read()
		if not res_cmd:
			res_cmd = b'success!'

	# 返回客户端消息
	udp_server.sendto(res_cmd, client_ip_port)
	# 如果发消息超过1024字节，这个报错是根据客户端收消息字节的限制，如果加大客户端的buffersize的话，就不会报错了。
	# 报错OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，或该用户用于接收数据报的缓冲区比数据报小。
	# 在Linux平台上则不会报错，直接接收1024字节的内容，其他丢弃。下次命令执行结果不会被上次打扰。
udp_server.close()

