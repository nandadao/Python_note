"""
    封装  --> 数据
        1.通过两个公开方法(不建议)
"""


# 1.私有化数据
# 4.



class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 22 <= value <= 65:
            self.__age = value
        else:
            raise Exception("我不要")
    # 类变量 -- > 覆盖实例变量
    # property  -- >拦截
    age = property(get_age, set_age)





