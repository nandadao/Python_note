"""
    抽象: 个体 --> 类别
          对象     类
          具体    抽象
          qtx      人

        设计:先有对象,再先有类.
        编码:先有类,再先有对象.
"""


class Wife:
    """
        创建老婆类,抽象的概念
    """
    # 1. 数据 -- 变量
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # 2. 行为 -- 方法(函数)
    def play(self):
        print(self.name, "在玩耍")

# 创建对象:类名(参数)
#         构造函数(参数) -->  __init__
w01 = Wife("铁锤",150,150)
w01.play()# 自动传递w01进入方法
