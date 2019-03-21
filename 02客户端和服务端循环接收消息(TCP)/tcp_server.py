#coding:utf-8
"""
模拟tcp服务端收发消息
"""
from socket import *
ip = '127.0.0.1'
port = 8888
backlog = 5 
buffersize = 1024 

tcp_server = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM 流式的套接字，代表TCP
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #这行的作用是为了防止端口为wait相关状态时，重启服务端会报错。SO_REUSEADDR代表重新使用ip和端口
tcp_server.bind((ip,port)) 
tcp_server.listen(backlog)

while True:
	print('服务端在等连接...')
	conn,c_addr = tcp_server.accept()
	print('接收到ip和port {} 的连接请求对象：{}==>'.format(c_addr,conn))

	while True:
		try:
			client_msg = conn.recv(buffersize) #当客户端断开连接时，此时情况要么是报一个异常（异常终止客户端会导致服务端报异常）或者一直收空（正常close客户端会导致服务端一直收空）
			if not client_msg:break #收空处理
		except Exception as e: #异常处理
			break

		print('客户端发过来一个消息 ==>',client_msg.decode('utf-8'))

		server_msg = '改造后的消息为：'+ client_msg.decode('utf-8')
		conn.send(server_msg.encode('utf-8'))


	conn.close()
tcp_server.close()

"""
发现系统存在大量wait状态的连接时，可以通过调整Linux内核参数来解决：
vi /etc/sysctl.conf
加入以下内容：
net.ipv4.tcp_syncookies = 1
# 表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；
net.ipv4.tcp_tw_reuse = 1
# 表示开启重用。允许将time_wait连接重新用于新的TCP连接，默认为0,表示关闭；
net.ipv4.tcp_tw_recycle = 1
# 表示开启TCP链接中的time_wait连接进行快速回收处理，默认为0,表示关闭；
net.ipv4.tcp_fin_timeout = 30
# 修改系统默认的TIMEOUT时间，超过此时间自动断开。
然后执行 /sbin/sysctl -p 让参数生效。
"""



