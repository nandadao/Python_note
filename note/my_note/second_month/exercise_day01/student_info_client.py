"""
    udp客户端
"""
from socket import *
import struct

# 服务端地址
ADDR = ("0.0.0.0", 9999)

#　创建udp套机字
sockfd = socket(AF_INET, SOCK_DGRAM)


while True:
    id = input("请输入学生的id:")
    if not id:
        break
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    height = float(input("请输入学生身高："))

    # 生成格式对象　　i->int  f---> float  s--> bytes
    st = struct.Struct("i20sif")

    # 数据打包
    data_bytes = st.pack(int(id), name.encode(), age, height)
    data = str(st.unpack(data_bytes))

    # 向服务器发送
    n = sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("From Server:", msg.decode())


sockfd.close()







