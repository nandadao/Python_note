"""
    http_server 2.0
    IO多路复用
    自己设计一个类
"""
from socket import *
from select import select



class HTTPServer:
    def __init__(self, host="0.0.0.0", port=8888, dir=None):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.dir = dir
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 直接创建套接字
        self.create_socket()

    # 创建套接字
    def create_socket(self):
        # 注意：属性可以在类的任何地方添加
        self.sockfd = socket()
        # 端口复用
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(self.address)

    # 启动法务
    def server_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d"%self.port)
        # IO多路复用
        # 循环地接收

        self.rlist.append(self.sockfd)
        while True:
            # 客户端连接才算，就绪，才可以放到r中
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            # print(rs)
            # 处理IO，也就是连接
            for r in rs:
                if r is self.sockfd:  # 这里指，有浏览器连接诶
                    c, addr = r.accept()  # ｃ是客户端的连接套接字
                    self.rlist.append(c)

                else:
                    # 处理具体请求
                    self.handle(r)

    # 处理客户端请求
    def handle(self, connfd):
        request = connfd.recv(4096).decode()
        print(request)






if __name__ == '__main__':
    # 通过HTTPServer类快速搭建服务
    # 通过该服务让浏览器访问到我的网页
    # 1.使用流程
    # 2.需要用户确定的内容

    # 用户决定的参数
    HOST = "0.0.0.0"
    PORT = 8000
    DIR = "./static"
    httpd = HTTPServer(HOST, PORT, DIR) # 生成对象
    httpd.server_forever()  # 启动服务




















