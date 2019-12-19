"""
httpserver 2.0
"""
from socket import *
from select import select

class HTTPServer:
    def __init__(self,host='0.0.0.0',port=80,dir=None):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.dir = dir
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 直接创建套接字
        self.create_socket()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               1)
        self.sockfd.bind(self.address)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d"%self.port)
        # IO多路服用方法监控IO
        self.rlist.append(self.sockfd)
        while True:
            rs,ws,xs=select(self.rlist,
                            self.wlist,
                            self.xlist)
            for r in rs:
                if r is self.sockfd:
                    # 浏览器链接
                    c,addr = r.accept()
                    self.rlist.append(c)
                else:
                    # 处理具体请求
                    self.handle(r)

    # 处理客户端请求
    def handle(self,connfd):
        request = connfd.recv(4096).decode()
        # 客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return

        # 解析请求，提取请求内容
        request_line = request.split('\n')[0]
        info = request_line.split(' ')[1]
        print(connfd.getpeername(),':',info)

        # 根据请求内容将其分为两类
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd,info)
        else:
            self.get_data(connfd,info)
        connfd.close()
        self.rlist.remove(connfd)

    def get_data(self,connfd,info):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += '\r\n'
        response += "<h1>Waiting for httpserver 3.0</h1>"
        connfd.send(response.encode())
    # 处理网页
    def get_html(self,connfd,info):
        if info == '/':
            # 要主页
            filename = self.dir+'/index.html'
        else:
            # 具体的网页
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += '\r\n'
            response += "<h1>Sorry....</h1>"
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += '\r\n'
            response += fd.read()
        finally:
            # 将响应发送给浏览器
            connfd.send(response.encode())

if __name__ == '__main__':
    # 通过HTTPServer类快速搭建服务
    # 通过该服务让浏览器访问到我的网页
    # 1. 使用流程
    # 2. 需要用户确定的内容

    # 用户决定的参数
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = './static'
    httpd = HTTPServer(HOST,PORT,DIR) # 生成对象
    httpd.serve_forever() # 启动服务