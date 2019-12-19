"""
    封装(保护)数据
        -- 通过两个公开方法(不建议)
"""
# 步骤
# 1. 私有化数据  --> 类外无法操作数据
# 2. 定义公开的读取方法 --> 在读取数据时做判定
# 3. 定义公开的写入方法 --> 在写入数据时做判定

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # 目的:保护成员不被类外操作
        # 私有化:使用双下划线命名
        # 障眼法:实际是 _类名 + 私有变量名
        #       _Wife__age
        # self.__age = age
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self,value):
        if 22 <= value <= 65:
            self.__age = value
        else:
            raise Exception("我不要")

w01 = Wife("锤锤",25)
w01.set_age(26)
print(w01.get_age())
# print(w01._Wife__age)
print(w01.__dict__)

