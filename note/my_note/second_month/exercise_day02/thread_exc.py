"""
使用多线程，同时从多个地方拷贝文件的某一部分，
最终在本地合成一个文件
提示：
    先探测，有几个路径有视频，则创建几个线程，
    注意顺序下载，要下载的文件终端输入

    １．先判断，哪些目录下有目标文件
    ２．有几个路径下有，就创建几个线程
    ３．每个线程负责一个路径，要选好下载文件的哪部分
    ４．多个线程下载的内容需要最后为一个文件
"""
# 文件是copy_movie.mp4

from threading import Thread,Lock
import os
from time import sleep

lock = Lock()
# 老师的答案
urls = [
    "/home/tarena/桌面/",
    "/home/tarena/模板/",
    "/home/tarena/音乐/",
    "/home/tarena/图片/",
    "/home/tarena/下载/",
    "/home/tarena/视频/",
]

filename = input("File:")
explorer = []  # 存储有目标文件的路径
for i in urls:
    # 查找那个路径有目标，然后存在explorer中
    if os.path.exists(i+filename):  #
        explorer.append(i+filename)

path_num = len(explorer)  # 有几处资源
if path_num == 0:
    print("没有资源")
    os._exit(0)
file_size = os.path.getsize(explorer[0])  # 获取文件大小
# 定下来每块文件的大小
block_size = file_size // path_num + 1  # 为了把文件全拷贝过来

# 本地文件打开
fd = open(filename, "wb")



# 拷贝文件
def load(path, num):
    """
    :param path:从哪个路径下载
    :param num: 要下载哪一部分
    """
    f = open(path, "rb")
    seek_bytes = block_size*num
    f.seek(seek_bytes)  # 从开头向后偏移seek_bytes个大小
    data = f.read(block_size)  # 这是下载过程的模拟
    # 写文件
    with lock:
        fd.seek(seek_bytes)
        # sleep(0.1)
        fd.write(data)





# 先创建线程
jobs = []
num = 0 # 表示第几块
for path in explorer:
    t = Thread(target=load, args=(path,num))
    jobs.append(t)
    t.start()
    num += 1

[i.join() for i in jobs]  # 回收线程



























# 自己的思路
# file = input("请输入要拷贝的文件：")
# # size = os.path.getsize(filename) 获取文件大小
#
#
# # 获取存在目标文件的路径数量
# def file_count():
#     count = 0
#     # 存在目标文件的路径列表
#     urls_file = []
#     for item in urls:
#         file_list = os.listdir(item)
#         for i in file_list:
#             if i == file:
#                 count += 1
#                 urls_file.append(item)
#     return (count, urls_file)
# # print(file_count()[1]) # ['/home/tarena/图片/', '/home/tarena/下载/', '/home/tarena/视频/']
#
# # 复制文件函数
# def copy_file():
#     for i in file_count()[1]:
#         size = os.path.getsize(i+file)
#         fr = open(i+file, "rb")
#         fr.seek()





# 创建线程
# for i in range(file_count()[0]):
#     th = Thread(target=fun)


















