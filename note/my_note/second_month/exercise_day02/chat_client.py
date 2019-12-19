# 聊天室
# 客户端
"""
    chat room client
"""
import sys
from socket import *
import os

# 服务器地址
# 老师的IP
# ADDR = ("172.40.91.233", 8888)
ADDR = ("127.0.0.1", 8888)

# 完成聊天功能
# 发送信息
def send_msg(s, name):
    while True:
        try:
            text = input("Msg>>")
        except KeyboardInterrupt:
            text = "quit"
        if text == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出群聊")

        # 类似"c %s %s"%(name, text)
        msg = "C {} {}".format(name, text)
        s.sendto(msg.encode(), ADDR)


# 接收信息
def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        if data == b"EXIT":
            sys.exit()
        print(data.decode() + "\nMsg>>", end="")


# 客户端启动函数
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    # 进入聊天室部分
    # s.sendto(b"L", ADDR)
    while True:
        name = input("请输入姓名：")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        # 得到结果
        data, addr = s.recvfrom(128)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break   # 如果成功就跳出循环，登录成功
        else:
            print("进入聊天室失败")

    # 收发消息, 子进程退出的时候，不会影响父进程，所以需要把父进程手动退出
    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        send_msg(s, name)   # 子进程发送
    else:
        recv_msg(s)  # 父进程接收




if __name__ == '__main__':
    main()















