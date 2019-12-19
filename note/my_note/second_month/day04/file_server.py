"""
    练习：选择一张图片，从客户端上传到服务端
        提示：
            １．客户端读取图片的内容
            ２．将内容发送给服务端
            ３．服务端接受图片内容
            ４．包粗拿在服务端某个位置（写入）
            （客户端边读边发，服务读边收边写）
            （客户端，服务端程序都要写）
"""


from socket import *
from time import localtime

# 设置一个全局变量,
SAVE_PATH = "/home/tarena/桌面/"

s = socket()
s.bind(("127.0.0.1", 8887))
s.listen(3)

# 连接客户端
c , addr = s.accept()
print("Connect from", addr)

# 打开文件
tmp = localtime()
img = "%s-%s-%s.jpg"%tmp[:3]

f = open(SAVE_PATH+img, "wb")

# 接受图片
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

# data = c.recv(9999999999)
# f.write(data)



f.close()
c.close()
s.close()

















