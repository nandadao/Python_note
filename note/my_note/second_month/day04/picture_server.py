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

from socket import  *

sockfd = socket()

sockfd.bind(("0.0.0.0", 9999))
sockfd.listen(3)

connfd, addr = sockfd.accept()

f = open("/home/tarena/桌面/pic.png", "wb")
while True:

    data = connfd.recv(1024)
    if not data:
        break
    f.write(data)






connfd.close()
sockfd.close()

f.close()














