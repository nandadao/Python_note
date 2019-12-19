"""
    练习
        创建模块exercise01
        使用三种方式，调用当前模块的成员fun01 fun02 fun03
"""

def fun01():
    print("module02 -- fun01")

class MyClass:
    def fun02(self):
        print("MyClass -- fun02")

    @classmethod
    def fun03(cls):
        print("MyClass -- fun03")



