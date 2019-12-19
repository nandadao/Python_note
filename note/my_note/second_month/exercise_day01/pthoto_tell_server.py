"""
### 扩展练习
要求：
１．通过  客户端 选择 图片向服务端发送。同时告知服务端   图片类型，
２．服务端利用接口，完成对图片的识别，并将最后的判断结果发送给客户端（发送最可能的结果）
考虑一下是否要把服务端收到的图片删除。
"""
# 服务端

from socket import *
import os
from baidu import baidu


sockfd = socket()
sockfd.bind(("0.0.0.0", 9999))
sockfd.listen(3)

connfd, addr = sockfd.accept()

f = open("recv_photo", "wb")

while True:
    data = connfd.recv(1024)
    if not data:
        break
    f.write(data)

f.close()

types = connfd.recv(1024)
print("类型是：", types)

#  图片已经传过来，进行图像识别


re = baidu(types, "recv_photo")
print("识别的结果是：", re[0][0])


# 识别之后删除传过来的图片
os.remove("recv_photo")




connfd.close()
sockfd.close()

























