from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,
             SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 创建epoll对象
p = epoll()

# 建立查找字典
fdmap = {s.fileno():s}

# 关注s套接字
p.register(s,EPOLLIN)

# 循环监控IO发生
while True:
    # 提交监控
    events = p.poll()
    print("你有新的IO需要处理哦")
    for fd,event in events:
        if fd == s.fileno():
            c,addr = s.accept()
            print("Connect from",addr)
            # 添加新的关注IO
            p.register(c,EPOLLIN|EPOLLERR|EPOLLET)  # 边缘触发
            fdmap[c.fileno()] = c  # 注意维护字典与register保持一致
        # elif event & EPOLLIN:
        #     # 通过文件描述符取得对象
        #     data = fdmap[fd].recv(1024).decode()
        #     if not data:
        #         p.unregister(fd) # 不再关注
        #         fdmap[fd].close()
        #         del fdmap[fd] # 从字典删除
        #         continue
        #     print(data)
        #     fdmap[fd].send(b'OK')