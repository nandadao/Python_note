"""
    模块相关知识点
"""
# 1. __all__变量：定义可导出成员，仅对from xx import *语句有效。
# from module02 import *
#
# fun01()
# MyClass.fun03()



from module02 import MyClass

# MyClass.fun03()

# 2. 模块对应的文件路径名。
# print(__file__)

# 3.__name__：真实的模块名（被导入模块）  __main__（主模块）
print(__name__)#  __main__
