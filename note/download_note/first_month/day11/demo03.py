"""
    封装(保护)数据
        -- 通过属性@property
    练习:module02.py
"""


# 步骤
# 1. 私有化数据  --> 类外无法操作数据
# 2. 定义公开的读取方法 --> 在读取数据时做判定
# 3. 定义公开的写入方法 --> 在写入数据时做判定
# 4. 使用@property修饰读取方法
#       @xxx.setter修饰写入方法
#             --> 将对数据的操作转为对方法的操作

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    @property  # age =  property(get_age,None)
    def age(self):
        return self.__age

    @age.setter  # age.setter(set_age)
    def age(self, value):
        if 22 <= value <= 65:
            self.__age = value
        else:
            raise Exception("我不要")

w01 = Wife("锤锤", 25)
w01.age = 26
print(w01.age)
