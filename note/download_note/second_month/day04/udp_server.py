"""
udp_server.py  udp服务端流程
重点代码
"""

from socket import *

# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr = ('0.0.0.0',8888)
sockfd.bind(server_addr)

# 收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    print("From %s Msg:%s"%(addr,data.decode()))
    sockfd.sendto(b'Thanks',addr)

# 关闭套接字
sockfd.close()









