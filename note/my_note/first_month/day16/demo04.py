"""
    迭代器
"""

class SkillManagerIterator:
    """
        迭代器
    """

    def __init__(self, data):
        self.__data = data
        self.__index = 0

    def __next__(self):
        # try:
        #     item =self.__data[self.__index]
        #     self.__index += 1
        #     return item
        # except:
        #     raise StopIteration

        if self.__index == len(self.__data):
            raise StopIteration()

        item =self.__data[self.__index]
        self.__index += 1
        return item


class SkillManager:


    """
        可迭代对象
    """
    def __init__(self):
        self.__list_skills = []

    def add_skill(self, skill):
        self.__list_skills.append(skill)

    def __iter__(self):
        return SkillManagerIterator(self.__list_skills)


manager = SkillManager()
manager.add_skill("九阳神功")
manager.add_skill("白骨")
manager.add_skill("乾坤")


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















