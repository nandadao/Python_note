"""
    继承 --  方法

    财产继承：钱不用孩子挣，但是可以花。
    皇位继承：江山不用孩子打，但是可以坐。
    代码继承：子类不用写，但是可以直接使用。

    抽象：从许多个事物中，舍弃个性、非本质的属性，抽出共性、本质的过程。
    练习:exercise01
"""


# 多个类，在概念上是一致的，且有相同的代码，
class Person:
    def say(self):
        print("说话")


class Student(Person):
    def study(self):
        print("学习")


class Teacher(Person):

    def teach(self):
        print("讲课")


# 子类对象，具有父类成员。
s01 = Student()
s01.say()
s01.study()

# 父类对象，不能使用子类成员。
p01 = Person()
p01.say()

# python 内置函数
# 学生对象s01 是一种 Student学生类型
print(isinstance(s01, Student))  # True
# 学生对象s01 是一种 Person人类型
print(isinstance(s01, Person))  # True
# 学生对象s01 是一种 Teacher老师类型
print(isinstance(s01, Teacher))  # False
# 人对象p01 是一种 Student学生类型
print(isinstance(p01, Student))  # False

# 学生类型 是一种 Student学生类型
print(issubclass(Student, Student))  # True
# 学生类型  是一种 Person人类型
print(issubclass(Student, Person))  # True
# Student 是一种 Teacher老师类型
print(issubclass(Student, Teacher))  # False
# Student 是一种 Student学生类型
print(issubclass(Person, Student))  # False

# 学生对象s01 是 Student学生类型
print(type(s01) == Student)  # True
# 学生对象s01 是 Person人类型
print(type(s01) == Person)  # False
# 学生对象s01 是 Teacher老师类型
print(type(s01) == Teacher)  # False
# 人对象p01 是 Student学生类型
print(type(p01) == Student)  # False
