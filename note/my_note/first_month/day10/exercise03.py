"""
    练习1：
        在终端中，循环录入学生信息（名字，年龄，性别，成绩）
        1.用类表达，创建一个类：学生类
        2.如果名字为空，结束录入，打印所有人的信息：
            行为：打印个人信息的行为
"""


class Student_Info:
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def print_self(self):
        print("我叫%s, 今年%d岁了， 性别%s,成绩是%d" % (self.name, self.age, self.sex, self.score))


# list_student = []
# while True:
#     name = input("请输入姓名：")
#     if name == "":
#         break
#     age = int(input("请输入年龄："))
#     sex = input("请输入性别：")
#     score = float(input("请输入成绩："))
#
#     stu = Student_Info(name, age, sex, score)
#     list_student.append(stu)
#
# for item in list_student:
#     item.print_self()


# 学生列表
list_student = [
    Student_Info("悟空", 27, "男", 100),
    Student_Info("八戒", 33, "男", 60),
    Student_Info("沙僧", 24, "男", 70),
    Student_Info("唐僧", 31, "女", 6),
]


# 1.定义函数，再学生列表中查找姓名是八戒的学生对象
#  测试：将对象的信息打印再终端中

# def find_bajie(list_input):
#     for item in list_input:
#         if item.name == "八戒":
#             return item
#
# re = find_bajie(list_student)
# if re:
#     re.print_self()


# 2.定义函数，再学生列表中查找成绩大于60分的所有学生对象
#  测试：将所有对象的信息打印再终端中

# def find_score_bigger_than_60(list_input):
#     list_result = []
#     for item in list_input:
#         if item.score > 60:
#             list_result.append(item)
#
#
# list_re = find_score_bigger_than_60(list_student)


# 3.定义函数，再学生列表中查找年龄大于30的所有学生对象
#  测试：将所有姓名打印再终端中
# 画内存图，

# def age_bigger_than_30():
#     list_name = []
#     for item in list_student:
#         if item.age > 30:
#             list_name.append(item)
#     return list_name
#
#
# for i in age_bigger_than_30():
#     print(i.name)


# 4.定义函数，再学生列表中查找成绩最低的学生对象
# #  测试：将该学生信息打印在终端中
# # 画内存图，

# def find_the_low_student():
#     low = list_student[0]
#     # index_low = 0
#     for item in range(1, len(list_student)):
#         if list_student[item].score < low.score:
#             low = list_student[item]
#             # index_low = item
#     return low
#
#
# find_the_low_student().print_self()

# [11, 2,33,4]
# 5.根据年龄按照升序将学生列表进行排序，                # 两层循环，需要练习
def fun01():
    # low = list_student[0]
    # for item in range(1, len(list_student)):
    #     if list_student[item].age < low.age:
    #         # low, list_student[item] = list_student[item], low
    #         low = list_student[item]
    for r in range(len(list_student)-1):  # 取出，不取最后一个，因为最后一个无法跟后面的数比较
        for c in range(r+1, len(list_student)):
            if list_student[r].age > list_student[c].age:
                list_student[r].age,list_student[c].age = list_student[c].age,list_student[r].age


fun01()
for i in list_student:
    print(i.age)




# 6.将学生列表中所有男同学删除

def delete_all():
    for i in range(len(list_student)-1, -1, -1):
        if list_student[i].sex == "男":
            del list_student[i]

delete_all()
for item in list_student:
    item.print_self()












