"""
    重写
        内置可重写函数
"""

class Car:
    def __init__(self, price=0):
        self.price = price

    # __str__ 下面的return 的返回值随意
    def __str__(self):
        return "ok"

    # __repr__ 后面的return 返回值，必须是机器可以理解的'Car("%d")'
    def __repr__(self):
        return 'Car(%d)'%self.price

c01 = Car(300)
print(c01)
print(c01.__repr__())

c02 = Car(500)





# 将字符串作为python代码执行  --> 灵活
# eval

# re = eval(input())
# print(re)






















