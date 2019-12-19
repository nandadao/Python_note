"""
    thread_event　互斥方法演示
"""
from threading import Thread, Event

s = None  # 用于通讯，共享资源
e = Event()  # 事件对象




def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()  # 解除阻塞

t = Thread(target=杨子荣)
t.start()

print("说对口令就是自己人")
e.wait() # 阻塞，直到用set()解除阻塞
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死......")

t.join()




















