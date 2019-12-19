"""
    对象计数器
    创建老婆类,记录老婆对象的数量.
"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print("我已经娶了%d个老婆了"%cls.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


w01 = Wife("锤锤")
w02 = Wife("方方")
w03 = Wife("圆圆")
Wife.print_count()
