"""
    继承 -- 数据
    练习:exercise02

"""

class Person:
    def __init__(self,name=""):
        self.name = name


"""
# 子类如果没有构造函数，使用父类构造函数。
class Student(Person):
    pass

s01 = Student("悟空")
print(s01.name)
"""


# 如果子类有构造函数，会覆盖父类构造函数。
# 必须调用父类构造函数
class Student(Person):
    def __init__(self, name="", score=0):
        super().__init__(name)# 调用父类构造函数
        self.score = score

# 执行的是子类构造函数
s01 = Student("悟空", 100)
print(s01.score)
print(s01.name)
