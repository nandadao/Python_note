"""
    tcp_server.py
    服务端
    重点代码，要求独立完成
"""

""""
    练习1：将两个程序改写为客户端可以不断的给服务端发送内容，收到ＯＫ　，如果客户端输入＃＃则两个程序豆结束
    练习２：一个客户端退出后，可以重新连接下一个客户端，继续工作
"""


import socket
from time import sleep

# 创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置端口立即重用
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定地址
sockfd.bind(("172.40.79.135", 9998))

# 设置监听
sockfd.listen(3)   # 3这个值设置多少都无所谓，因为linux已经自动设置了

# 处理客户端连接
while True:
    print("Waiting for connect ...")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        print("Server Exit")
        break
    except Exception as e:
        print(e)
        continue


    while True:
    # 收发消息
        data = connfd.recv(2)
        if not data:
            # 客户端断开，recv返回空字节串
            break
        # if data.decode() == "##":
        #     break
        print("Recv:", data.decode())

        n = connfd.send(b"OK-\n")    # 一定要发送字节串
        print("send %d bytes"%n)
# 关闭套接字
    connfd.close()  # 对应这个客户端的套接字关闭掉

sockfd.close()


# 本地连接
# telnet 127.0.0.1 9999
















