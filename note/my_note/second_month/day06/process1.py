"""
    process进程创建方法
"""
import multiprocessing as mp
from time import sleep

a = 1

# 除了这个函数，子进程不执行其他任何代码
def fun():
    sleep(2)
    print("子进程函数")

# 实例化进程对象
p = mp.Process(target=fun)
# 启动进程，执行target绑定的函数
# start执行后，子进程才被创建
p.start()

sleep(3)
print("父进程")


# 回收进程，防止子进程变成僵尸进程，阻塞，等待回收
p.join()

"""
上面13,16,18三行代码与下方一样
p = os.fork()
if p == 0:
    fun()
    os._exit()
else:
    os.wait()
"""

















