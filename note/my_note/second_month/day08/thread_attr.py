"""
    线程属性
"""
from threading import Thread
from time import sleep

def fun():
    sleep(15)
    print("线程对象属性")

t = Thread(target=fun, name="Tarena")   # 添加线程名称


# 主线程退出分支线程也退出
# t.setDaemon(True)



# t.start()
# 获取线程
t.start()
t.setName("Tedu")
print("Name:", t.getName())
print("is alive:", t.is_alive())

# t.join()
























