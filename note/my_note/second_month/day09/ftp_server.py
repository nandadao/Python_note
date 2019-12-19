"""
    ftp服务单
    ftp文件处理
    env:python3.6
    多线程并发 & socket
"""
import sys
from socket import *
import os, sys
import signal
from threading import Thread
import time

#　全局变量（很多地方都要用到的）
HOST = "0.0.0.0"
PORT = 8080
ADDR = (HOST, PORT)

FTP = "/home/tarena/FTP/"

# 实现文件传输的具体功能
class FTPServer(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    # 处理文件列表发送
    def do_list(self):
        # 获取文件列表
        files_list = os.listdir(FTP)
        if not files_list:
            self.connfd.send("文件库为空".encode())
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1) # 防止ok与后面的文件列表粘包
        # 发送文件列表
        files = "\n".join(files_list)  # 按照\n把列表拼接为一个字符串
        self.connfd.send(files.encode())

    # 处理下载文件
    def do_retr(self, filename):
        try:
            # 根据，能否打开文件判断是否有这个文件
            f = open(FTP+filename, "rb")
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)  # 防止粘包
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
        f.close()

    # 处理上传文件
    def do_stor(self,filename):
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已经存在".encode())
            return
        else:
            self.connfd.send(b"OK")
        # 接受文件
        f = open(FTP + filename, "wb")
        # 循环接收
        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                # 文件发送完成
                break
            f.write(data)
        f.close()



    def run(self):
        while True:
            # 循环接收客户端请求
            data = self.connfd.recv(1024).decode()
            if not data or data == "QUIT":
                return
            elif data == "LIST":
                self.do_list()
            elif data[:4] == "RETR":
                filename = data.split(" ")[-1]
                self.do_retr(filename)
            elif data[:4] == "STOR":
                filename = data.split(" ")[-1]
                self.do_stor(filename)




# 创建tcp多线程并发
def main():
    # 创建tcp套接字
    s = socket()
    # 复用端口
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    print("Listen the port 8080...")
    # 循环接收客户端连接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from ", addr )
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建线程
        t = FTPServer(c)
        t.setDaemon(True)
        t.start()



if __name__ == '__main__':
    main()













































