"""
    包

项目根目录--普通文件夹
包--文件夹
    模块--文件
        类--class
            函数--def
                语句--命令


# 导入模块成功的唯一条件：
# sys.path + 导入路径 可以正确定位模块

import sys
sys.path.append('/home/tarena/month01/day15/my_project')

"""
# 导入方式1
# import package01.p1
# package01.p1.fun01()

# import package01.p1 as p
# p.fun01()

# 导入方式2
# from package01.package02.p2 import fun02
# fun02()

# 导入方式3
# from package01.package02.p2 import *
# fun02()

# 如果导入路径是一个包，那么需要在包的__init__.py模块中设置__all__属性
from package01.package02 import *
p2.fun02()



