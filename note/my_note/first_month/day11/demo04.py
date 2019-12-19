"""
    封装：设计角度
        类与类之间的调用的三种方法
"""

# 需求：老张开车去东北   # 考得是面向对象


# 写法1：每次去东北，都会创建新车
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#
#     def go_to(self, pos):
#         print("去", pos)
#         # 新车
#         car = Car()
#         car.run()
#
#
# class Car:
#     def run(self):
#         print("汽车行驶...")
#
# lz01 = Person("老张")
# lz01.go_to("东北")




# # 2.常见写法2：老张开着自己的车，去东北，去北京
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#         self.car = Car()
#
#     def go_to(self, pos):
#         print("去", pos)
#         # 新车
#         self.car.run()
#
#
# class Car:
#     def run(self):
#         print("汽车行驶...")
#
#
# lz01 = Person("老障")
# lz01.go_to("东北")
# lz01.go_to("北京")




# 方法3：老张去东北的工具，以来于外部传入。
class Person:
    def __init__(self, name=""):
        self.name = name


    def go_to(self, car, pos):
        print("去", pos)
        # 新车
        car.run()


class Car:
    def run(self):
        print("汽车行驶...")


lz01 = Person("老障")
bm = Car()
lz01.go_to(bm, "东北")
# lz01.go_to("北京")













