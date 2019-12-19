"""
编程：
​	使用Process创建两个子进程，
    同时复制一个文件，分别复制前半部分和后半部分，形成
​	两个新文件
    以 字节数 判断前后两个部分，１０的话就是前５后５
"""
from multiprocessing import Process
import os

filename = "/home/tarena/图片/荷花.jpeg"
size = os.path.getsize(filename)


# 复制上半部分
def top():
    fr = open(filename, "rb")
    fw = open("top.jpg", "wb")
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 赋值下半部分
def bot():
    fr = open(filename, "rb")
    fw = open("bot.jpg", "wb")
    fr.seek(size//2, 0) # 以开头为开始，向后移动size//2个字节
    fw.write(fr.read())
    fr.close()
    fw.close()




p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()
p1.join()
p2.join()





















