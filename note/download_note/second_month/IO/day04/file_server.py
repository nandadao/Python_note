"""
练习 ： 选择一张图片，从客户端上传到服务端

       温馨提示： 客户端读取图片的内容
                 将内容发送给服务端
                 服务端接受图片内容
                 保存在服务端某个位置
"""
from socket import *
from time import localtime

# 存在这里
SAVE_PATH = "/home/tarena/图片/"

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

# 打开文件
tmp = localtime()
img = "%s-%s-%s.jpg"%tmp[:3]
f = open(SAVE_PATH+img,'wb')

#接受图片
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()














