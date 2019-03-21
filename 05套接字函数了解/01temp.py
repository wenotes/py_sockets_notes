# 公共用途套接字函数
# s.sendall() #发送完整的TCP数据（本质就是循环调用send，在待发送数据量大于己端套接字缓冲区空间时，数据不丢失，循环调用send直到发完）
# s.getpeername() #获取当前连接的远端地址
# s.getsockname() #获取自己套接字地址
# s.getsockopt()  #返回指定套接字参数
# s.setsockopt()  #设定套接字参数
# 面向锁的套接字方法
# s.setblocking() #设置套接字阻塞与非阻塞模式
# s.settimeout() #设置阻塞套接字操作的超时时间
# s.gettimeout() #获取阻塞套接字操作的超时时间
# 面向文件的套接字函数
# s.fileno() #套接字的文件描述符
# s.makefile() #创建一个与该套接字相关的文件