
# from socket import *
#
# s = socket()
# s.bind(("0.0.0.0", 9999))
# s.listen(3)
#
# c, addr = s.accept()
# print("Connect from", addr)
# request = c.recv(4096).decode()  # 接受请求
# print(request)
#
# response = """HTTP/1.1 200 OK
# Content-Type:text/html;charset=UTF-8
#
# 人生苦短，我用Python
# """
# c.send(response.encode())
#
# c.close()
# s.close()

import os
from time import sleep


pid = os.fork()
if pid < 0:
    print("Create proces failed")
elif pid == 0:
    sleep(3)
    print("The new process")
else:
    sleep(4)
    print("The old process")

print("Fork test over")









































