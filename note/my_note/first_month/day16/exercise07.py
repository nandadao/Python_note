"""
    练习:
        自定父MyRange类，实现下列效果(给出一个数，输出01234)
"""


class MyRangeIterator:
    def __init__(self, data=0):
        self.data = data
        self.__count = 0

    def __next__(self):
        if self.__count < self.data:
            re = self.__count
            self.__count += 1
            return re
        else:
            raise StopIteration()


class MyRange:
    def __init__(self, number=0):
        self.__number = number

    def __iter__(self):
        return MyRangeIterator(self.__number)


for item in MyRange(5):
    print(item)  # 0 1 2 3 4

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























