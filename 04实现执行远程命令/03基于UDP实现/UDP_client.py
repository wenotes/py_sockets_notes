#coding:utf-8
"""
客户端发送远程命令
"""
from socket import *

ip_port = ('127.0.0.1',8889)
buffersize = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

print('UDP客户端启动..')
while True:
	cmd = input('>>>').strip()
	if cmd=='exit':
		break
	# 发消息
	udp_client.sendto(cmd.encode('utf-8'), ip_port)

	# 收消息
	cmd_res,server_ip_port = udp_client.recvfrom(buffersize)
	print('UDP服务端返回的命令执行结果↓↓\n', cmd_res.decode('gbk'))

udp_client.close()

