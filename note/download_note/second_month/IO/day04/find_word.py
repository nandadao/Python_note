"""
提供查找单词服务
使用udp编程完成
从客户端循环输入单词，获得单词的解释
服务端负责提供这个解释
"""

from socket import *


# 查单词函数
def select_word(word):
    f = open('dict.txt')  # 文本方式打开

    # 每次获取一行
    for line in f:
        w = line.split(' ')[0]
        if w > word:
            f.close()
            return "没有该单词"
        elif word == w:
            # 查到单词
            f.close()
            return line
    else:
        f.close()
        return "没有该单词"

sockfd = socket(AF_INET,SOCK_DGRAM)
server_addr = ('0.0.0.0',8888)
sockfd.bind(server_addr)

while True:
    data,addr = sockfd.recvfrom(128)
    print("Word:",data.decode())
    # 查找单词
    text = select_word(data.decode())
    sockfd.sendto(text.encode(),addr)

sockfd.close()


