"""
    练习:
        创建模块exercise01
        使用三种方式,调用当前模块的成员fun01 fun02  fun03
"""
# 11:30
# 方式１:
# import module02
# module02.fun01()
#
# c01 = module02.MyClass()
# c01.fun02()
#
# module02.MyClass.fun03()

# 方式2:
# from module02 import fun01
# from module02 import MyClass
# fun01()
#
# c01 = MyClass()
# c01.fun02()
#
# MyClass.fun03()

# 方式3
from module02 import *

fun01()

c01 = MyClass()
c01.fun02()

MyClass.fun03()




