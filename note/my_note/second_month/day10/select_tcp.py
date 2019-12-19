"""
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
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

# select只能放对象，不能放方法
# 设置关注的IO
rlist = [s]  # 等待被连接，读　IO行为
wlist = []
xlist = []


while True:
    # 循环监控s, 等待客户端连接
    # 客户端连接才算，就绪，才可以放到r中
    rs, ws, xs = select(rlist, wlist, xlist)
    # print(rs)
    # 处理IO，也就是连接
    for r in rs:
        if r is s:
            # 又有新的客户端连接
            c, addr = r.accept()  # ｃ是客户端的连接套接字
            print("Connect from", addr)
            rlist.append(c)


        else:
            # 某个客户端给服务端发送消息了
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)  # 不再关注这个IO
                r.close()  # 客户端套接字关闭
                continue   # 不处理这个IO，继续处理下一个IO
            print(data)
            # r.send(b"OK")
            wlist.append(r) # 加入写IO

    for w in ws:
        w.send(b"OK")
        wlist.remove(w)































