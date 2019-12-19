"""

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


# 学生列表
list_student = [
    Student("悟空", 27, "男", 100),
    Student("八戒", 30, "男", 60),
    Student("沙僧", 33, "男", 70),
    Student("唐僧", 20, "女", 65),
]


# 1. 定义函数,在学生列表中查找姓名是八戒的学生对象
#    测试,将对象的信息打印在终端中
def find01():
    for item in list_student:
        if item.name == "八戒2":
            return item


stu = find01()
if stu:
    stu.print_self()  # None.print_self()


# 2. 定义函数,在学生列表中查找成绩大于60分的所有学生对象
#    测试,将所有对象的信息打印在终端中
def find02():
    list_result = []
    for item in list_student:
        if item.score > 60:
            list_result.append(item)
    return list_result


for item in find02():
    item.print_self()


# 3. 定义函数,在学生列表中查找成所有年龄大于30的学生姓名
#    测试,将所有姓名打印在终端中
def find03():
    list_name = []
    for item in list_student:
        if item.age > 30:
            list_name.append(item.name)
    return list_name


for item in find03():
    print(item)


# 4. 定义函数,在学生列表中查找成绩最低的学生对象
#    测试,将该学生信息打印在终端中
def find04():
    min_stu = list_student[0]
    for i in range(1, len(list_student)):
        if min_stu.score > list_student[i].score:
            min_stu = list_student[i]
    return min_stu


re = find04()
re.print_self()


# 5. 根据年龄,按照升序将学生列表进行排列.
def sort():
    for r in range(len(list_student) - 1):
        for c in range(r + 1, len(list_student)):
            if list_student[r].age > list_student[c].age:
                list_student[r], list_student[c] = list_student[c], list_student[r]


sort()
for item in list_student:
    item.print_self()


# 6. 将学生列表中所有男同学删除.
def delete_all():
    for i in range(len(list_student) - 1, -1, -1):
        if list_student[i].sex == "男":
            del list_student[i]


delete_all()
print("------")
for item in list_student:
    item.print_self()
