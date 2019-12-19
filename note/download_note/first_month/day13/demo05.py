"""
    反向运算符(特别不重要)
        作用：当前类对象与其他类对象做算数运算
"""
class Vector1:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return "向量的分量是：" + str(self.x)

    def __add__(self, other):
        return Vector1(self.x + other)

    def __radd__(self, other):
        return Vector1(self.x + other)

v01 = Vector1(10)
print(v01 + 10)#v01.__add__(10)
print(10 + v01)# v01.__radd__(10)