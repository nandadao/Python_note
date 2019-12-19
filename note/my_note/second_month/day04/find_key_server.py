"""
    练习：
        １．使用udp编程完成，从客户端输入一个单词，获得单词的解释
        2.服务端负责提供这个解释
        3.注意功能的封装

        提示：
            单词本放在服务端中，
"""

from socket import *

# 查点此函数
def find_key(word):
    f = open("/home/tarena/note/do/dict.txt", "r")

    # word = input("请输入要查询的单词：")

    for line in f:
        w = line.split(" ")[0]
        # print(line.split(" "))
        if w > word:
            f.close()
            # print("没有该单词")
            return "没有该单词"
            # break
        if w == word:
            f.close()
            # print(line)
            return line
            # break

    else:
        # print("没有该单词")
        return "没有该单词"



ADDR = ("0.0.0.0", 9999)

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(ADDR)

while True:

    data, addr = sockfd.recvfrom(1024)

    # 查单词封装成函数：功能＼参数＼返回值：这三个自己设计
    text = find_key(data.decode())

    sockfd.sendto(text.encode(), addr)


sockfd.close()












