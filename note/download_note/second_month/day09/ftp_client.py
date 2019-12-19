"""
ftp 文件服务 客户端
"""
from socket import *
import sys,time

# 服务器地址
ADDR = ('127.0.0.1',8080)

# 客户端处理类
class FTPClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    # 获取文件列表
    def do_list(self):
        self.sockfd.send(b'LIST') # 发送请求 29
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 一次接收所有文件名称字符串(解决沾包)
            data = self.sockfd.recv(1024 * 1024 * 10)
            print(data.decode())
        else:
            print(data)

    def do_retr(self,filename):
        # 发送请求
        self.sockfd.send(('RETR '+filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            f = open(filename,'wb')
            # 循环接收
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    # 文件发送完
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    def do_stor(self,filename):
        try:
            f = open(filename,'rb')
        except Exception:
            print("文件不存在")
            return
        # 提取文件名称
        filename = filename.split('/')[-1]
        # 发送请求
        self.sockfd.send(('STOR ' + filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'QUIT')
        self.sockfd.close()
        sys.exit('谢谢使用')

# 网络链接
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    ftp = FTPClient(sockfd) # 调用请求功能

    # 循环的发送请求
    while True:
        print("==========命令选项============")
        print("*****      LIST       *****")
        print("*****  STOR filename  *****")
        print("*****  RETR filename  *****")
        print("*****      QUIT       *****")
        print("=============================")
        cmd = input("命令:")
        if cmd == 'LIST':
            ftp.do_list()
        elif cmd[:4] == 'RETR':
            filename = cmd.split(' ')[-1]
            ftp.do_retr(filename)
        elif cmd[:4] == 'STOR':
            filename = cmd.split(' ')[-1]
            ftp.do_stor(filename)
        elif cmd == 'QUIT':
            ftp.do_quit()
        else:
            print("请输入正确命令！")

if __name__ == '__main__':
    main()

