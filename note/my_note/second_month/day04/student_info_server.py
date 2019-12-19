"""
	作业：
​	使用udp和struct完成，
​	１．从客户端循环录入学生信息，信息包含
​	id   姓名　年龄	身高
​	２．将信息打包发送给服务端
​	３．在服务端将学生信息写到一个文件中，每个学生信息占１行
　＊　重点代码要求自己写出来：
"""

"""
    udp服务端
"""
from socket import *

# 创建udp套接字/数字报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)


# 绑定地址
server_addr = ("0.0.0.0", 9999)
sockfd.bind(server_addr)

f = open("file", "w")


# 收发消息
while True:
    print("等待客户端发送信息：")
    data, addr = sockfd.recvfrom(1024)
    # print("收到写入信息：", data.decode())
    if not data:
        break
    f.write(data.decode())
    f.write("\n")
    f.flush()


    # print("From %s Meg:%s"%(addr, data.decode()))

    n = sockfd.sendto(b"Thanks",addr)



# 关闭套接字
sockfd.close()
f.close()





















