#coding:utf-8
"""
"""
from socket import *
from time import sleep

ip = '127.0.0.1'
port = 8888

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect((ip,port))

# 快速的发送了 间隔短消息少 的数据
tcp_client.send(b'hello server fuck you !')

sleep(2)
tcp_client.close()

"""
由此可看出：
	数据量超出buffersize设置数，会导致粘包，而且如果数据量非常大，tcp会通过优化算法，拆分数据量，进行分批发送，也就意味着客户端的套接字缓冲区不一定就收到全部的数据。当你recv的时候也就只能收到部分数据。
	消息间隔短数据量少也会导致粘包

自此，我们要自己来解决这个问题
"""