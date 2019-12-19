"""
    功能 ： 类似qq群功能
    【1】 有人进入聊天室需要输入姓名，姓名不能重复
    【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
    【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
    【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
    【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxx
    chat room AID 1910
    env: python3.6
    author: Qian
    socket  udp  &  fork
    三引号是文档说明
"""
# 服务端
from socket import *
import os, sys


# 服务地址（所有函数都要使用的，有意义的变量设计成全局变量）
ADDR = ("0.0.0.0", 8888)

# 存储用户信息（全局变量）{name:[address,num]}
user = {}

# 敏感词汇
words = ["蔡徐坤", "xx", "oo", "qq"]

# 黑名单
ips = []

# 警告判断
def warn(name, text):
    for word in words:
        if word in text:
            user[name][1] += 1
            return False
    return True






# 函数三要素，功能/参数/返回值

# 登录功能：
def do_login(s, name, addr):
    if name in user or "管理" in name or addr[0] in ips:
        s.sendto(b"FAIL", addr)
        return
    s.sendto(b"OK", addr)
    # 通知其他人
    msg = "\n欢迎%s进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(), user[i][0])  # 通过键取出地址
    # 将其添加到用户字典
    user[name] = [addr, 0]   # 以name为键，地址为值




# 聊天
def do_chat(s, name, text):
    if not warn(name, text):
        if user[name][1] >= 3:
            msg = "\n%s 踢出群聊"%name
            ips.append(user[name][0][0])

            for i in user:
                # 刨除本人，把消息发送给其他人
                if i != name:
                    s.sendto(msg.encode(), user[i][0])
                else:
                    s.sendto(b"EXIT", user[name][0])
            del user[name]

        msg = "警告 %s 请你善良"%name
        s.sendto(msg.encode(), user[name][0])
    else:
        msg ="\n%s : %s"%(name, text)
        for i in user:
            # 刨除本人，把消息发送给其他人
            if i != name:
                s.sendto(msg.encode(), user[i][0])


# 退出：删除用户，告知其他人
def do_quit(s, name):
    msg = "\n%s退出了群聊"%name
    for i in user:
        if i != name:
            # 告知其他人
            s.sendto(msg.encode(), user[i][0])
        else:
            # 让他本人的接收进程退出
            s.sendto(b"EXIT", user[i][0])
    del user[name]



# 功能分发函数(这个函数一直执行，)
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        # 处理，　根据发来的data进行响应的处理（登录，聊天，退出等）
        # 根据请求内容，选择功能模块去处理
        tmp = data.decode().split(" ", 2)   # ２只切前两个空格，后面的不切割了
        # 切割后选择第一个["L", "name"]
        # L   C   Q
        if tmp[0] == "L":
            # 登录
            do_login(s, tmp[1], addr)   # 具体函数处理具体功能
        elif tmp[0] == "C":
            # 把消息发送给其他用户
            do_chat(s, tmp[1], tmp[2])
        elif tmp[0] == "Q":
            do_quit(s, tmp[1])


# 启动函数
def main():
    # udp网络服务器
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        # 子进程实现管理员消息的发送
        # print(user)  # {}这里是空的
        while True:
            text = input("管理员消息：")
            msg = "C 管理员 " + text
            # 将消息从子进程发送给父进程
            s.sendto(msg.encode(), ADDR)

    else:
        do_request(s)  # 让父进程处理请求


# 为程序测试的语句
if __name__ == '__main__':
    main()


























