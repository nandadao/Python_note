
# 服务器
from socket import *

# http使用tcp协议
s = socket()
s.bind(("0.0.0.0", 8000))
s.listen(3)

c, addr = s.accept()  # 连接了浏览器
print("Connect from", addr)
request = c.recv(4096)
print(request.decode())    # 打印出请求
request_01 = request.decode().split(" ")[1]


f = open("index.html", "r")
data = f.read()

if request_01 == "/":
    response = """HTTP/1.1 200 OK
    Content-Type:text/html;charset=UTF-8
    
    %s
    """%data
else:
    response = """HTTP/1.1 404 Not Found
    Content-Type:text/html;charset=UTF-8

    Sorry     # 这是响应体
    """

c.send(response.encode())  # 发送响应

c.close()
s.close()

















