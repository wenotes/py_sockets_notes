#coding:utf-8
"""
"""
import socket, time

c_st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


c_st.connect(('127.0.0.1',8888)) #与服务端连接

time.sleep(2)

c_st.send('你好！我是客户端。'.encode('utf-8'))

time.sleep(2)

msg = c_st.recv(2048)
print('服务端返回的消息: {}'.format(msg.decode('utf-8')))

time.sleep(2)
