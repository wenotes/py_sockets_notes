#coding:utf-8
"""
数据量少且间隔短测试不粘包
"""
from socket import *

ip_port = ('127.0.0.1',8889)

udp_client = socket(AF_INET, SOCK_DGRAM)

print('UDP客户端启动..')
# 发消息
udp_client.sendto(b'hello udp server fuck your uncle!', ip_port)
udp_client.sendto(b'hello udp server fuck your uncle!', ip_port)
udp_client.sendto(b'hello udp server fuck your uncle!', ip_port)

udp_client.close()

