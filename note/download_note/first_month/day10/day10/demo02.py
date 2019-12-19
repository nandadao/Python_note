"""
    实例成员
        记住一句话:实例成员,使用对象地址访问.
"""


# 全局变量
# name = "铁锤"

# 局部变量
# def fun01():
#     name = "铁锤"

class Wife:
    def __init__(self, name):
        # 创建实例变量 self.name
        self.name = name

    def play(self):
        # 读取实例变量
        print(self.name, "玩耍")


w01 = Wife("铁锤")
# 读取实例变量
print(w01.name)
# 可以通过__dict__操作所有实例变量
# 修改实例变量
w01.name = "锤锤"

# print(w01.__dict__)
# w01.__dict__["name"] = "锤锤"
# print(w01.name)

w01.play()  # 自动将w01传入方法
# Wife.play(w01)# 也可以用类名调用,但是不建议.

"""
# 可以在类外创建实例变量(不建议)
class Wife:
    pass

w01 = Wife()
# 创建实例变量
w01.name = "铁锤"
# 读取实例变量
print(w01.name)
"""

"""
# 可以在类中其他方法内实例变量(不建议)
class Wife:
    def __init__(self):
        self.fun01()

    def fun01(self):
        self.name = "铁锤"
 
w01 = Wife()
print(w01.name)
"""
