#coding:utf-8
"""

"""
import socket, time

# 1、创建一个服务端的socket实例
s_st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET  代表网络通信
# socket.SOCK_STREAM 基于TCP协议的

# 2、绑定一个地址，ip:port
ip = '127.0.0.1'
port = 8888
s_st.bind((ip,port)) #地址必须写成元组的形式

# 3、
backlog = 5 #半连接池，设置连接等待数。请求先进入半连接池，服务端依次接待客户端的连接。
s_st.listen(backlog)

# 4、建立链接，你会拿到客户端的链接和地址
print('服务端在等客户端链接...')
conn,c_addr = s_st.accept()
print('服务端接收到客户端 {} 的连接 ==>'.format(c_addr))

time.sleep(2)

# 5、收消息，用链接去收，返回一个消息
buffersize = 1024 #代表字节数
msg = conn.recv(buffersize)
print('客户端发过来一个消息 ==>',msg.decode('utf-8'))
time.sleep(2)

# 6、服务端返回信息，也就是服务端发消息
conn.send('你好！我是服务端。'.encode('utf-8'))
time.sleep(2)

# 7、关闭与客户端的链接
conn.close()
# 8、关闭socket链接
s_st.close()


# 有人会有疑问，服务端能否先发消息。答案是肯定的。只不过，在一般的场景下都是由客户端先发出消息，服务端后接收消息，然后根据服务端的要求返回指定的消息或服务。

