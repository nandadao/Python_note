"""
    封装(保护)数据
        -- 通过property
"""
# 步骤
# 1. 私有化数据  --> 类外无法操作数据
# 2. 定义公开的读取方法 --> 在读取数据时做判定
# 3. 定义公开的写入方法 --> 在写入数据时做判定
# 4. 类变量指向property对象 --> 将对数据的操作转为对方法的操作

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age

    def get_age(self):
        return self.__age

    def set_age(self,value):
        if 22 <= value <= 65:
            self.__age = value
        else:
            raise Exception("我不要")

    # 类变量 --> 覆盖实例变量
    # property --> 拦截
    age = property(get_age,set_age)


w01 = Wife("锤锤",25)
# w01.set_age(26)
w01.age = 26
print(w01.age)

