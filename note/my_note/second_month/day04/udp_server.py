"""
    udp服务端
"""
from socket import *

# 创建udp套接字/数字报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)


# 绑定地址
server_addr = ("0.0.0.0", 9999)
sockfd.bind(server_addr)


# 收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    print("From %s Meg:%s"%(addr, data.decode()))

    n = sockfd.sendto(b"Thanks",addr)



# 关闭套接字
sockfd.close()




















