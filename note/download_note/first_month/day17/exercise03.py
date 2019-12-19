"""
    练习：定义my_enumerate函数，实现下列效果。
    for index, item in my_enumerate(dict02):
        print(index, item)
"""


def my_enumerate(iterable):
    index = 0
    for item in iterable:
        yield (index, item)
        index += 1


list01 = [5, 6, 78, 5, 7]
dict02 = {"a": 1, "b": 2, "c": 3}
for index, item in my_enumerate(list01):
    print(index, item)
