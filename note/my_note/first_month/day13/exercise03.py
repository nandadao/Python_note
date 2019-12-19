"""
    练习：
        1.创建学生类(姓名，年龄，成绩)
        2.直接将学生对象输出到终端print(学生对象)
            格式：我是 孙悟空  今年   88岁， 考了 100分
        3.将学生对象克隆一份，改变其中一个对象信息，打印出来看看是否改变
"""

class Student:
    def __init__(self, name="", age=0, score=0):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "我是%s,今年%d岁.考了%d分" % (self.name, self.age, self.score)

    def __repr__(self):
        return 'Student("%s",%d,%d)'%(self.name, self.age, self.score)

s01 = Student("悟空", 22, 100)
print(s01)

s02 = Student("唐僧", 23, 99)
print(s02.__repr__())

print(s02)



s03 = eval(s02.__repr__())
s02.score = 88
print(s03)



















