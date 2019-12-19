"""
    进程池使用演示
    进程池：作用
    大量函数需要频繁销毁，创建，
    先写事件函数，后创建进程池
    父进程结束，进程池销毁
"""
from multiprocessing import Pool
from time import sleep, ctime, time

start = time()
# 进程池事件函数
def worker(msg):
    sleep(2)
    print(ctime(), "--", msg)
    return 200

# 创建进程池，进程池事件，必须写在上面

pool = Pool(4)  # 不写参数，默认使用机器所有内核

# 向进程池中添加事件
for i in range(10):
    msg = "Tedu %d"%i
    r = pool.apply_async(func=worker, args=(msg,))  # args传的是元组


# 关闭进程池
pool.close()

# 回收进程池
pool.join()
# print(r.get())    # 获取进程池的返回值
end = time()
print(end-start)



















