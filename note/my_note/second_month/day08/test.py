"""
    测试多线程与多进程对比
"""

# 计算性
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


# ＩＯ
def io():
    write()
    read()

def write():
    f = open("test", "w")
    for i in range(1800000):
        f.write("Hello world\n")
    f.close()

def read():
    f = open("test", "r")
    lines = f.readlines()
    f.close()























