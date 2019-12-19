"""
ftp文件处理
env: python3.6
多线程并发 & socket
"""
from socket import *
from threading import Thread
import sys,os
import time

# 全局变量
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST,PORT)
FTP = "/home/tarena/FTP/" # 文件库位置

# 实现文件传输的具体功能
class FTPServer(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    # 处理文件列表发送
    def do_list(self):
        # 获取文件列表
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send('文件库为空'.encode()) #19
            return
        else:
            self.connfd.send(b'OK') #19
            time.sleep(0.1)
        # 发送文件列表
        files = '\n'.join(file_list)
        self.connfd.send(files.encode())

    # 文件下载
    def do_retr(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except Exception:
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()

    # 处理上传文件
    def do_stor(self,filename):
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        f = open(FTP+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                # 文件发送完
                break
            f.write(data)
        f.close()

    def run(self):
        while True:
            # 接收客户端请求
            data = self.connfd.recv(1024).decode()
            if not data or data == 'QUIT':
                return # 线程结束
            elif data == 'LIST':
                self.do_list()
            elif data[:4] == 'RETR':
                filename = data.split(' ')[-1]
                self.do_retr(filename)
            elif data[:4] == 'STOR':
                filename = data.split(' ')[-1]
                self.do_stor(filename)


# 搭建网络模型
def main():
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    print("Listen the port 8080...")
    # 循环接收客户端链接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue

        #  创建线程处理
        t = FTPServer(c)
        t.setDaemon(True)  # 主线程退出其他线程也退出
        t.start()

if __name__ == '__main__':
    main()






