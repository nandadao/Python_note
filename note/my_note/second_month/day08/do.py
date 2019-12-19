"""
    时间装饰器
"""

# import time
# # 装饰器
# def timeis(f):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = f(*args, **kwargs)
#         end_time = time.time()
#         print("%s运行时间%.6f"%(f.__name__, end_time-start_time))
#     return wrapper
#
#
#
# @timeis
# def fun1(s):
#     print("hello", s)
#
#
# fun1("世界")

# # 判断质数
# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


from threading import Thread, Lock
import os
from time import sleep

lock = Lock()
urls =[
    "/home/tarena/桌面/",
    "/home/tarena/模板/",
    "/home/tarena/音乐/",
    "/home/tarena/图片/",
    "/home/tarena/下载/",
    "/home/tarena/视频/",
]

filename = input("File:")
explorer = [] # 存储有目标文件的路径
for i in urls:
    # 查找那个路径有目标，然后放入加explorer
    if os.path.exists(i+filename):
        explorer.append(i + filename)

path_num = len(explorer)
if path_num == 0:
    print("没有资源")
    os._exit(0)

# 获取文件大小
file_size = os.path.getsize(explorer[0])
# 定下来每块文件的大小
block_size = file_size//path_num + 1

fd = open(filename, "wb")

# def load()













