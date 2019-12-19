from socket import *

s = socket()
s.connect(("127.0.0.1", 8887))

img = input(">>")


f = open(img, "rb")
# 边读取边发送
while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

# data = f.read()
# s.send(data)



f.close()
s.close()











