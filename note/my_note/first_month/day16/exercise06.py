"""
    定义员工管理器，记录多个员工
    迭代员工管理器，获取多个员工
    要求：1.体会推导过程
         2.画出迭代器架构设计图
"""


class EmployeeManagerIterator:
    def __init__(self, list_employee):
        self.__count = 0
        self.list_employee = list_employee

    def __next__(self):
        if self.__count == len(self.list_employee):
            raise StopIteration()
        item = self.list_employee[self.__count]
        self.__count += 1
        return item


class EmployeeManager:
    def __init__(self):
        self.__list_employee = []

    def add_employee(self, employee):
        self.__list_employee.append(employee)

    def __iter__(self):
        return EmployeeManagerIterator(self.__list_employee)


manager = EmployeeManager()
manager.add_employee("唐僧")
manager.add_employee("八戒")
manager.add_employee("孙悟空")
manager.add_employee("沙僧")

for item in manager:
    print(item)

# # for循环原理
# # 1.获取迭代器
# iterator = list01.__iter__()
# while True:
#     try:
#         # 2.获取下一个元素
#         item = iterator.__next__()
#         print(item)
#     # 3.如果没有元素则结束循环
#     except StopIteration:
#         break




"""
    面向对象：
        三大特征：
            1.封装
            2.继承
            3.多态
        六大原则：
            1.开闭原则（目标、总的指导思想）
                对扩展开放，对修改关闭
                增加新功能不改变原有代码
            2.单一原则（类的设计原则）
                一个类有且只有一个改变的原因
            3.依赖倒置（依赖抽象）
                
                抽象不依赖细节，细节依赖抽象
            4.
    
"""










