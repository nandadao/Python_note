"""
    select_test.py
    select　函数示例
"""
from select import select
from socket import *
from time import sleep


s = socket()
s.bind(("127.0.0.1", 8888))
s.listen(3)   # 如果没有客户端连接，select会阻塞


f = open("file", "r") # w+ 打开，自动创建


print("IO监控")
sleep(5)
rs, ws, xs = select([s,f], [f], [])
print("rlist", rs)
print("wlist", ws)
print("xlist", xs)

























