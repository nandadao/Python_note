"""
select tcp服务
重点代码
【1】将关注的IO放入对应的监控类别列表
【2】通过select函数进行监控
【3】遍历select返回值列表，确定就绪IO事件
【4】处理发生的IO事件
"""
from socket import *
from select import select

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,
             SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 设置关注的IO
rlist = [s] # s的读IO行为
wlist = []
xlist = []

while True:
    # 循环监控s
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            # 又有新的客户端链接
            c, addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)
        else:
            # 某个客户端给我发消息
            data = r.recv(1024).decode()
            if not data:
                # 客户端断开
                rlist.remove(r) # 不再关注这个IO
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r) #加入写IO

    for w in ws:
        w.send(b'OK')
        wlist.remove(w)















