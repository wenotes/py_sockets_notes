#coding:utf-8
"""
认证客户端连接合法性
"""
from socket import *
import os,hmac

secret_key = b'rangniheiheihei'

def auth_conn(conn):
	# 认证合法性
	auth_bytes = os.urandom(32) #产生32位随机字节
	conn.send(auth_bytes) #发送给客户端，客户端也会进行下面的哈希运算加盐，得到一个digest
	h = hmac.new(secret_key, auth_bytes) #哈希验证，给auth_bytes加盐
	digest = h.digest()

	from_c_res = conn.recv(len(digest)) #接收客户端的digest
	return hmac.compare_digest(from_c_res, digest) #将客户端返回的digest和自己的digest比较，一样返回True

def request_handle(conn,buffersize):
	# 通信循环
	if not auth_conn(conn):
		print('连接不合法，关闭连接，等待新连接')
		conn.close()
		return
	print('连接合法，开始进行通信...')
	while True:
		try:
			client_msg = conn.recv(buffersize) 
			if not client_msg:break 
		except Exception as e: 
			break
		print('客户端发过来一个消息 ==>',client_msg.decode('utf-8'))

		server_msg = '改造后的消息为：'+ client_msg.decode('utf-8')
		conn.send(server_msg.encode('utf-8'))

def server_handle(ip_port,buffersize=1024,backlog=5):
	# 连接循环
	tcp_server = socket(AF_INET, SOCK_STREAM) 
	tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
	tcp_server.bind((ip_port)) 
	tcp_server.listen(backlog)

	while True:
		print('服务端在等连接...')
		conn,c_addr = tcp_server.accept()
		print('接收到ip和port {} 的连接请求对象：{}==>'.format(c_addr,conn))

		request_handle(conn,buffersize)

		conn.close()
	tcp_server.close()

if __name__ == '__main__':
	ip_port = ('127.0.0.1',8888)
	
	server_handle(ip_port)