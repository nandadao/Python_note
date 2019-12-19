"""
    将迭代器版本的员工管理器，改为yield版本
    day16/exercise04
    调试，体会过程.
"""
class EmployeeManager:

    def __init__(self):
        self.__list_employees = []

    def add_employee(self, skill):
        self.__list_employees.append(skill)

    def __iter__(self):
        # yield "悟空"
        # yield "八戒"
        # yield "唐僧"
        for item in self.__list_employees:
            yield item

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