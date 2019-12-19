"""
tcp_server.py 服务端
"""
import socket

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8888))

# 设置监听
sockfd.listen(3)

# 处理客户端链接
print("Waiting for connect...")
connfd,addr = sockfd.accept()
print("Connect from",addr)

# 收发消息
data = connfd.recv(1024)
print("Recv:",data)
n = connfd.send(b"OK\n") # 发送字节串

# 关闭套接字
connfd.close()
sockfd.close()

# 客户端测试命令 telnet 127.0.0.1 8888


