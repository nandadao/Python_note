"""
tcp_server.py 服务端
重点代码
"""
import socket

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8887))

# 设置监听
sockfd.listen(3)

# 处理客户端链接
while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        print("Server Exit")
        break
    except Exception as e:
        print(e)
        continue

    # 收发消息
    while True:
        data = connfd.recv(1024)
        if not data:
            # 客户端断开recv返回空字节串
            break
        # if data == b'##':
        #     break
        print("Recv:",data.decode())
        n = connfd.send(b"OK\n") # 发送字节串
        print("send %d bytes"%n)
    connfd.close() # 对应这个客户端的套接字关闭

# 关闭套接字
sockfd.close()

# 客户端测试命令 telnet 127.0.0.1 8888


