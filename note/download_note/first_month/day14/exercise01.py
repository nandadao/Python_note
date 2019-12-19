"""
    11:30
    练习：
        定义员工管理器
            1. 存储所有员工
            2. 提供计算总薪资的方法
        普通员工：底薪
        程序员:底薪 + 项目分红
        测试员：底薪 + Bug数*5
        需求变化：
            销售...
        要求：指出代码体现的三大特征与六个原则。
            特征：
                封装：员工管理器、程序员、测试员、普通员工
                继承：普通员工
                多态：程序员、测试员重写普通员工的计算薪资方法
            原则：
                开闭：增加新员工，不改变员工管理器
                单一：员工管理器(记录、总薪资)、程序员(计算薪资)、测试员...
                依赖倒置：员工管理器调用普通员工，而不调用具体员工(程序员/测试员)
                组合复用：员工管理器和具体员工(程序员/测试员)是组合关系
                里氏替换：add_employee参数是普通员工，传递是具体员工
                        具体员工重写时，调用了父类计算薪资方法(扩展重写)
                迪米特：员工管理器、程序员、测试员、普通员工 互不影响
"""


class EmployeeManager:
    def __init__(self):
        self.__all_employee = []

    def add_employee(self, emp):
        self.__all_employee.append(emp)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__all_employee:
            total_salary += item.calculate_salary()
        return total_salary


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        """
            计算薪资
        :return: 数值类型，表示薪资。
        """
        return self.base_salary

# --------------------------

class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # self.base_salary +  self.bonus
        result = super().calculate_salary() + self.bonus
        return result


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() + self.bug_count * 5

# ------------
manager = EmployeeManager()
manager.add_employee(Programmer(10000,200000))
manager.add_employee(Tester(8000,2000))
manager.add_employee(Employee(5000))

print(manager.get_total_salary())