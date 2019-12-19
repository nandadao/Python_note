from socket import *
from multiprocessing import Process
import sys,signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("Listen the port 8888...")
# 循环接收客户端链接
while True:
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print(e)
        continue

    #  创建进程处理
    p = Process(target=handle,args=(c,))
    p.daemon = True # 父程退出其他线程也退出
    p.start()







