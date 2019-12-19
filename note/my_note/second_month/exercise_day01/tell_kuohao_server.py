"""
    ## 提高练习
知识点涵盖：
文件读写
网络套接字传输
数据逻辑处理
封装思想
基础逻辑
### 题目要求
１．编写一组程序，分为 客户端和 服务端
２．客户端用于与用户交互，用户可以通过input()选择一个文本文件（存在大量的括号内容()  {}  []  ,
    但是这些括号可能存在匹配不正确的情况），将这个文件发送给服务端
３．服务端需要判断发过来的文件中括号匹配是否正确，如果正确则给客户端回   复完全正确的信息，
    如果不正确，需要告知客户端  不正确，并且   指出括号不正确的位置
​	比如：此时客户端会收到："在第１８个字符位置　{   不正确"

提示：
    怎么判断括号，以及括号的位置



"""
#　服务端
from socket import *
from time import sleep


def tell_kuohao(file_addr):
    list_left = ["(", "[", "{"]
    list_right = [")", "]", "}"]
    list_all = ["()", "[]", "{}"]
    list_save = []
    f = open(file_addr, "r")
    data = f.read()
    for item in data:  # 遍历带有括号的字符串，然后
        if item in list_left:
            list_save.append(item)   # 把左边的括号放到一个列表中
        elif item in list_right:
            str_all = list_save[-1] + item
            list_save.pop(list_save[-1])
            if str_all in list_all:
                continue
            return "在第%d个字符位置　%s 不正确"%(data.index(item), item)
    if len(list_save) != 0:
        return "在第%d个字符位置　%s 不正确"%(data.index(list_save[0]), list_save[0])



    f.close()


sockfd = socket(AF_INET, SOCK_STREAM)
# 设置端口立即重用
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(("0.0.0.0", 9998))
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

    f = open("file_kuohao.txt", "wb")
    while True:
    # 收发消息
        data = connfd.recv(1024)
        if not data:
            break
        # if data.decode() == "##":
        #     break
        f.write(data)
        f.close()

        re = tell_kuohao("file_kuohao.txt")

        n = connfd.send(re.encode())    # 一定要发送字节串
        print("send %d bytes"%n)
# 关闭套接字
    connfd.close()  # 对应这个客户端的套接字关闭掉












sockfd.close()
























