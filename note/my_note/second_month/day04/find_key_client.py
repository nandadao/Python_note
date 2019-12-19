
from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

ADDR = ("0.0.0.0", 9999)

while True:
    key = input("请输入要查询的单词：")
    if not key:
        break
    sockfd.sendto(key.encode(), ADDR)

    data, addr = sockfd.recvfrom(1024)
    print("单词和解释：",data.decode())



sockfd.close()
















