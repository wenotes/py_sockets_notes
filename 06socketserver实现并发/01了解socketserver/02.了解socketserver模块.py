# coding:utf-8
"""
socketserver是通用套接字服务器类。通过socket进行的封装
这个模块试图捕获定义服务器的各个方面:

基于套接字的服务器:
	家庭地址:
		- AF_INET{，6}: IP (Internet Protocol)套接字(默认)
		- AF_UNIX: Unix域套接字
		-其他的，例如AF_DECNET是可以想象的(see <socket.h>)
	套接字类型:
		- SOCK_STREAM(可靠的流，例如TCP)
		- SOCK_DGRAM(数据报，如UDP)

对于基于请求的服务器(包括基于套接字的服务器):
	
	-客户端地址验证后再进一步查看请求(这实际上是一个钩子，用于任何需要查看的处理在任何其他事情之前(例如记录)应要求)

	-如何处理多个申请:
		-同步(一次处理一个请求)
		-分叉(每个请求由一个新进程处理)
		-线程化(每个请求由一个新线程处理)

这个模块中的类偏爱最简单的服务器类型写:同步TCP/IP服务器。这是一个糟糕的类设计，
但是节省一些打字。(还有一个问题是深层的类层次结构减慢方法查找。)

继承图中有五个类，其中四个类表示四种类型的同步服务器:
        +------------+
        | BaseServer | 这是基类
        +------------+
              |
              v
        +-----------+        +------------------+
        | TCPServer |------->| UnixStreamServer | 流
        +-----------+        +------------------+
              |
              v
        +-----------+        +--------------------+
        | UDPServer |------->| UnixDatagramServer | 数据报
        +-----------+        +--------------------+



server类：处理连接
"BaseServer", "TCPServer继承于base", "UDPServer继承于tcp", 
"UnixStreamServer","UnixDatagramServer",

request类：处理通信
"BaseRequestHandler", "StreamRequestHandler继承于base","DatagramRequestHandler继承于base"

跟并发有关：forking 进程，threading 线程
"ThreadingUnixStreamServer","ThreadingUnixDatagramServer"
"ForkingUDPServer","ForkingTCPServer",
 "ThreadingUDPServer", "ThreadingTCPServer",
"""

