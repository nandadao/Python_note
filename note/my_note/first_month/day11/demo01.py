"""
    封装  --> 数据
        1.通过两个公开方法(不建议)
"""


# 1.私有化数据



class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # 私有化：使用双下划线命名
        # 目的：保护成员不被类外操作
        # 障眼法：实际是  _类名 + 私有变量名
        #              _Wife__age
        # self.__age = age
        self.set_age(age)

    def get_age(self):

        return self.__age

    def set_age(self, value):
        if 22 <= value <= 65:
            self.__age = value
        else:
            raise Exception("我不要")



w01 = Wife("锤锤", 89)
w01.__age =99
# print(w01.__age)
print(w01.__dict__)
# print(w01._Wife__age)
