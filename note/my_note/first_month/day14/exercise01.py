"""
    练习：
        定义员工管理器
            1.存储所有员工
            2.提供计算总薪资的方法
        普通员工：底薪
        程序员：底薪+项目分红
        测试员：底薪+Bug数*5
        需求变化：
            销售...

        要求：
            1.画图
            2.写代码
            3.指出三大特征，六大原则
                特征：
                    封装：员工管理器、程序员、测试员、普通员工
                    继承：普通员工
                    多态：程序员、测试
"""

class EmployeeManager:
    def __init__(self):
        self.__all_employee = []  #加下划线，自己用

    def add_employee(self, emp):
        self.__all_employee.append(emp)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__all_employee:
            total_salary += item.calculate_salary()
        return total_salary


class Employee:
    def __init__(self, base_salary=0):
        self.base_salary = base_salary   # 把子 类 的共性放到 父类 这里
    def calculate_salary(self):
        """
            计算薪资
        :return: 数值类型，表示薪资
        """
        return self.base_salary

# ------------------------------------


class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        result = super().calculate_salary() + self.bonus
        return result



class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        super().calculate_salary()
        return self.base_salary + self.bug_count*5


# ------------------------测试
manager = EmployeeManager()
manager.add_employee(Programmer(100000, 200000))
manager.add_employee(Tester(8000, 2000))
manager.add_employee(Employee(5000))

print(manager.get_total_salary())






# class PersonManager:
#     def __init__(self):
#         self.__list_person = []
#
#     def add_person(self, target):
#         self.__list_person.append(target)
#
#     def get_total_money(self):
#         total_money = 0
#         for item in self.__list_person:
#             total_money += item.calculate_money()
#         return total_money
#
# class Person:
#     def calculate_money(self):
#         pass
#
# # ----------------------------
# class CommonPerson(Person):
#     def __init__(self, compensation=0):
#         self.compensation = compensation
#     def calculate_money(self):
#         return self.compensation
#
# class ItPerson(Person):
#     def __init__(self, compensation=0, get_money=0):
#         self.compensation = compensation
#         self.get_money = get_money
#
#     def calculate_money(self):
#         return self.compensation + self.get_money
#
# class TestPerson(Person):
#     def __init__(self, compensation=0, bugs=0):
#         self.compensation = compensation
#         self.bugs = bugs
#
#     def calculate_money(self):
#         return self.compensation + self.bugs*5


























