"""
    复习
        封装
            数据角度：将多个基本数据类型 --> 一个自定义数据类型
                    例如：老婆(姓名,年龄,身高..) 敌人(...)
            行为角度：对外提供必要的功能,隐藏(私有化)实现的细节。
                    保护数据
                        核心思想：私有化数据
                                 提供两个读写方法
            设计角度：
                分而治之：将需求分解为多个类
                变则疏之：将(行为)变化点单独定义在类中
                           类与类：行为不同
                           对象与对象：数据不同
                ************
                高内聚：小而精的类
                低耦合：类关系松散
"""

"""
# 写法1：读写属性
class Wife:
    def __init__(self, age=0): 
        self.age = age

    @property#   age = property(读取方法age,None)
    def age(self):
        return self.__age

    @age.setter # age.setter(写入方法age)
    def age(self, value):
        self.__age = value 

w01 = Wife(88)
print(w01.age)
"""

"""
# 2. 只读属性
class Wife:
    def __init__(self):
        self.__weight = 100

    @property
    def weight(self):
        return self.__weight


w01 = Wife()
# w01.weight = 120
print(w01.weight)
"""

"""
# 3. 只写属性
class Wife:
    def __init__(self, age=0):
        self.age = age

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value
            print(self.__age)
        else:
            raise Exception("我不要")

    age = property(None, set_age)

w01 = Wife(25)
w01.age = 26
# print(w01.age)
"""
