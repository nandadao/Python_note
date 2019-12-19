"""
### 扩展练习
要求：
１．通过  客户端 选择 图片向服务端发送。同时告知服务端   图片类型，
２．服务端利用接口，完成对图片的识别，并将最后的判断结果发送给客户端（发送最可能的结果）
考虑一下是否要把服务端收到的图片删除。
"""

# 客户端
from socket import *

sockfd = socket()

sockfd.connect(("0.0.0.0", 9999))

f = open("/home/tarena/图片/边牧.jpeg", "rb")

while True:
    data = f.read(1024)
    if not data:
        break
    sockfd.send(data)


sockfd.send("动物".encode())




f.close()

sockfd.close()


















