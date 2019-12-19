# 客户端
from socket import *


sockfd = socket()
server_addr = ("0.0.0.0", 9998) # 服务器地址
sockfd.connect(server_addr)

while True:
# 发消息收消息
    addr = input("请输入文件地址：")
    f = open(addr, "rb")
    data = f.read(1024)
    if not data:
        break
# 发送给服务端（因为服务端是先收后发消息，所有客户端是先发消息后收消息）
    sockfd.send(data)  # 发送必须要发送字节串
    # if data == "##":
    #     break
    data_recv = sockfd.recv(1024)
    print("错误信息", data_recv.decode())   # 通过decode()把字节串转换成字符串


# 关闭套接字
sockfd.close()





















