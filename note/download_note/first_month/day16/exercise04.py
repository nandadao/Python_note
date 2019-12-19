"""
    练习:
        定义员工管理器，记录多个员工。
        迭代员工管理器，获取多个员工。
        要求：体会推导过程
             画出迭代器架构设计图
"""


class EmployeeManagerIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = 0

    def __next__(self):
        if self.__index == len(self.__data):
            raise StopIteration()

        item = self.__data[self.__index]
        self.__index += 1
        return item

class EmployeeManager:

    def __init__(self):
        self.__list_employees = []

    def add_employee(self, skill):
        self.__list_employees.append(skill)

    def __iter__(self):
        iterator = EmployeeManagerIterator(self.__list_employees)
        return iterator

manager = EmployeeManager()
manager.add_employee("悟空")
manager.add_employee("八戒")
manager.add_employee("唐僧")

for item in manager:
    print(item)

# iterator = manager.__iter__()
# while True:
#     try:
#         # 2. 获取下一个元素
#         item = iterator.__next__()
#         print(item)
#     # 3. 如果没有元素则结束循环
#     except StopIteration:
#         break
