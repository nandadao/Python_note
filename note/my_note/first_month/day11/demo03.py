"""
    通过属性：
        @property属性保护
"""


# 1.私有化数据
# 4.



class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age

    @property
    def age(self):  # age = property(get_age, None)
        return self.__age

    @age.setter
    def age(self, value):
        if 22 <= value <= 65:
            self.__age = value
        else:
            raise Exception("我不要")
    # 类变量 -- > 覆盖实例变量
    # property  -- >拦截






