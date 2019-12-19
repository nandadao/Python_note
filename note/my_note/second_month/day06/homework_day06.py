"""
编程：
​	使用Process创建两个子进程，
    同时复制一个文件，分别复制前半部分和后半部分，形成
​	两个新文件
    以 字节数 判断前后两个部分，１０的话就是前５后５
"""
from multiprocessing import *
file_addr = "/home/tarena/test/test.txt"
f = open(file_addr, "r")
data = f.read()

file_len = len(data)

# 读文件的上半部分,例如，打开的文件有１５个字节，７
def fun1():
    f1 = open("1.txt", "w")
    str_1 = data[:file_len//2]
    f1.write(str_1)
    f1.close()


# 读文件的下半部分
def fun2():
    f2 = open("2.txt", "w")
    str_2 = data[file_len//2:len(data)]
    f2.write(str_2)
    f2.close()



p = Process(target=fun2)
p.start()
fun1()

p.join()

f.close()

















