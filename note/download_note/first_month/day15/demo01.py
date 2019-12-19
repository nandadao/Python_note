"""
   模块

"""

def fun01():
    print("demo01 - fun01")


fun01()

# 导入方式1:import 模块名
# 本质：创建变量名，关联该模块。
import module01
module01.fun02()
module01.fun01()

# 导入模块时，可以起一个别名
# import module01 as m
# m.fun02()

# 导入方式2:from 模块 import 成员
# 本质：将该模块成员导入到当前作用域中
# from module01 import fun02
# fun02()

# 导入方法3: from 模块 import *
# 小心：导入的成员命名冲突
# from module01 import *
# fun02()
# fun03()
# fun01()# 调用的不是自己的，而是module01的。









