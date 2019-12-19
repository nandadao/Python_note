"""
	fork_server.py 基于fork的多进程服务
"""
from socket import *
import os
import signal

ADDR = ("0.0.0.0", 8888)

# 处理客户端请求
def handle(c):
	while True:
		data = c.recv(1024)
		if not data:
			break
		print("收到消息：", data.decode())
		c.send("服务端发给客户端的消息".encode())
	c.close()

# 创建tcp套接字
s = socket()
# 复用端口
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

# 处理僵尸进程产生
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen the port 8888...")
while True:
	# 循环接收客户端连接
	try:
		c, addr = s.accept()
		print("Connect from ", addr)
	except KeyboardInterrupt:
		s.close()  # 不写也行，系统自动回收
		os._exit(0)
	except Exception as e:
		print(e)
		continue
	
	# 客户端连接处理
	pid = os.fork()
	if pid == 0:
		# 处理请求
		s.close()  # 因为子进程用不到s，所以关闭
		handle(c) # 处理具体请求
		os._exit(0)  # 子进程结束后，退出，不用执行其他部分
		# 处理完请求子进程结束
	else:
		c.close()  # 父进程不需要c，所以先关闭
		continue # 父进程循环回去继续等待其他客户端，写不写continue都行























