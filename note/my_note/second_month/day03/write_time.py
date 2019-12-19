"""
    练习：
    编写一个程序，向一个文件中不断写入如下内容：
        1.2019-1-1  18：18：18
        2.2019-1-1  18：18：20
        3.2019-1-1  18：18：22
        4.2019-1-1  18：18：24

        5
    要求：每次写入占一行
         这是一个死循环，但是可以实时查看写入内容(open(a,f,1))
         当程序推出，重新启动后，书写内容能够衔接之前序号内容
"""

# import time
#
# f = open("file", "a+")
#
# f.seek(0)   # 把文件偏移量放到最开始
# n = 1
# for i in f:
#     n += 1  # 确定n的初始值
#
# while True:
#     time.sleep(2)
#     msg = "%d. %s\n"%(n, time.ctime())
#     f.write(msg)
#     f.flush()   # 刷新缓冲区
#     n += 1

# ======================================自己的答案


import time

f = open("file", "a+")  # 写入模式打开，然后根据行进行刷新

f.seek(0)

count = 1
for i in f:
    count += 1




while True:
    tuple_time = time.localtime()
    str_time = "%d.%d-%d-%d  %d:%d:%d%s"%(count, tuple_time[0],tuple_time[1],tuple_time[2],
                                     tuple_time[3],tuple_time[4],tuple_time[5],"\n")
    f.write(str_time)
    f.flush()
    time.sleep(2)
    count += 1


#
#
# f.close()






















