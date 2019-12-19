"""
    客户端
    tcp_client.py
"""

from socket import *

# 创建套接子
sockfd = socket()  # 创建ＴＣＰ　套接字（默认参数就是ＴＣＰ）

# 连接服务器
server_addr = ("127.0.0.1", 8888) # 服务器地址
sockfd.connect(server_addr)

while True:
# 发消息收消息
    data = input("Msg>>")
    if not data:
        break

# 发送给服务端（因为服务端是先收后发消息，所有客户端是先发消息后收消息）
    sockfd.send(data.encode())  # 发送必须要发送字节串
    # if data == "##":
    #     break
    data = sockfd.recv(1024)
    print("Server:", data.decode())   # 通过decode()把字节串转换成字符串


# 关闭套接字
sockfd.close()



















