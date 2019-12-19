"""
    epoll_erver.py
"""


from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)


# 创建epoll对象
p = epoll()

# 建立查找字典
fdmap = {s.fileno():s}

# 关注套接字
p.register(s,EPOLLIN)


# 循环监控IO发生
while True:
    # 提交监控
    events = p.poll()
    print(events)
    for fd, event in events:
        if fd == s.fileno():
            c, addr = s.accept()
            print("Connect from", addr)
            p.register(c, EPOLLIN|EPOLLERR)  # 添加新的关注IO
            fdmap[c.fileno()] = c   # 注意委会字典与register保持一致
        elif event & EPOLLIN:   # 如果是POLLIN类型IO则返回的是真
            # 通过文件描述符取得对象
            data =  fdmap[fd].recv(1024).decode()
            if not data:  # 如果客户端退出的话
                p.unregister(fd)  # 不再关注该IO
                fdmap[fd].close()  # 关闭此套接字
                del fdmap[fd]  # 从字典删除
                continue
            print(data)
            fdmap[fd].send(b"OK")

























































