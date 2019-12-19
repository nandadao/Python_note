"""
    继承 - 设计角度
"""
# 老张开车去东北
# 需求变化：
#         坐飞机
#         坐火车
#         骑车...

# 面向对象设计原则：
# 1. 开闭原则
#     开放              关闭
#  允许增加新功能    不能修改以前的代码
# 2. 依赖倒置
#    使用父，不使用子。

# 三大特征：
# 继承：抽象变化 --> 统一变化  --> 隔离变化
# 多态：重写父类方法 --> 传递子类对象
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle, pos):
        print("去", pos)
        if type(vehicle) ==  Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("汽车行驶...")

class Airplane:
    def fly(self):
        print("飞喽...")


lz01 = Person("老张")
c01 = Car()
a01 = Airplane()
lz01.go_to(c01, "东北")
