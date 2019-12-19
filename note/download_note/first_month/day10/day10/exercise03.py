"""
    练习1:
        在终端中循环录入学生信息(名字,年龄,性别,成绩),
        如果名字为空,结束录入,打印所有人的信息.
        -- 创建学生类
        -- 打印个人信息的行为
"""

class Student:
    """
        学生
    """

    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def print_self(self):
        print("我叫%s,今年%d岁了,性别%s,成绩是%d." % (self.name, self.age, self.sex, self.score))


list_studnet = []
while True:
    name = input("请输入姓名:")
    if name == "":
        break
    age = int(input("请输入年龄:"))
    sex = input("请输入性别:")
    score = float(input("请输入成绩:"))
    stu = Student(name, age, sex, score)
    list_studnet.append(stu)

for item in list_studnet:
    item.print_self()
