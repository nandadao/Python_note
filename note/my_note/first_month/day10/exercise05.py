"""
    对象，计数器
    创建老婆类，记录老婆对象数量
"""

class Wife:

    count = 0
    @classmethod
    def count_wife(cls):
        pass


    def __init__(self, name):
        self.name = name
        Wife.count += 1

w01 = Wife("1")
w02 = Wife("2")
print(Wife.count)
























