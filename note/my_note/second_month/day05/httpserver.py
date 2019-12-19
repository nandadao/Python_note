"""
练习：
编写一个服务端http程序，在客户端发起request请求时，
将网页按照http响应格式发送给浏览器展示
提示：网页内容是响应体，注意写响应格式
提高：对请求做一定的解析判断，如果请求内容是　/  ,则发送这个网页
​			如果是其他的则用　　404 进行
"""
from socket import *


# 处理浏览器请求
def handle(connfd):
    # http请求
    request = connfd.recv(4096).decode()
    # 从http请求中提取请求内容
    request_line = request.split("\n")[0]  # 取出请求行
    info = request_line.split(" ")[1]
    print(info)

    # 根据请求内容组织响应
    if info == "/":
        response = "HTTP/1.1 200 OK\r\n"  # 双引号需要自己手动添加，\r\n
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        with open("index.html") as f:
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"  # 双引号需要自己手动添加，\r\n
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "Sorry Not Fount"

    # 将响应发送给浏览器
    connfd.send(response.encode())




# 搭建tcp网络
def main(addr):
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口复用

    sockfd.bind(addr)
    sockfd.listen(3)


    while True:
        try:
            # 等浏览器连接
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            break
        handle(connfd)   # 处理浏览器请求

    sockfd.close()

if __name__ == "__main__":
    main(("0.0.0.0", 8000))



















