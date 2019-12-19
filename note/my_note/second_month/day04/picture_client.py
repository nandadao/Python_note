

from socket import  *

sockfd = socket()

address = ("127.0.0.1", 9999)
sockfd.connect(address)


f = open("/home/tarena/pic.png", "rb")

while True:
    data_pic = f.read(1024)
    if not data_pic:
        break
    sockfd.send(data_pic)







sockfd.close()
f.close()






















