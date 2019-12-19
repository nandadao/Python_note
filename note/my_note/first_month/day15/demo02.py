"""
    包

项目根目录----普通文件夹
包----文件夹
    模块-----文件
        类---class
            函数--def
                语句---命令

"""

# import package01.p1
#
# package01.p1.fun01()

# 方式一
# import package01.p1 as p
# p.fun01()


# 方式二
# from package01.package02.p2 import fun02
# fun02()


# 方式三
# from package01.package02.p2 import *
# fun02()

# 如果导入路径是一个包，那么需要在包的__init__.py模块中设置__all__属性
from package01.package02 import *
p2.fun02()











