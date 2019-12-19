"""
    需求：
        1. 定义函数，在老婆列表中查找所有老婆的姓名
        2. 定义函数，在老婆列表中查找所有老婆的姓名和身高
    需求：
        1. 定义函数，在老婆列表中累加所有老婆的总身高
        2. 定义函数，在老婆列表中累加所有老婆的总体重
    步骤：
        1. 将需求完整实现到函数中。
        2. 将变化点单独定义到函数中。
        3. 将通用代码定义到函数中。
        4. 用参数隔离变化点。
        5. 将通用代码移动到IterableHelper类中
        6. 测试调用IterableHelper的静态方法执行功能。

"""
from common.iterable_tools import IterableHelper



class Wife:
    """
        抽象的数据
    """

    def __init__(self, name="", age=0, height=0, weight=0):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.age, self.height, self.weight)


list01 = [
    Wife("铁锤", 27, 190, 200),
    Wife("铁钉", 37, 165, 160),
    Wife("铁棒", 24, 160, 190),
    Wife("铁锅", 23, 190, 100),
]


def condition01(item):
    return item.age > 25


def condition02(item):
    return item.height < 180


for item in IterableHelper.find_all(list01, condition01):
    print(item)

# ---------------------练习1-----------------------------
"""
def select01():
    for item in list01:
        yield item.name

def select02():
    for item in list01:
        yield (item.name,item.height)
"""


def handle01(item):
    return item.name


def handle02(item):
    return (item.name, item.height)


handle01(Wife("铁锤", 27, 190, 200))

"""
def select(func):
    for item in list01:
        # yield (item.name,item.height)
        # yield handle02(item)
        yield func(item)
"""

for item in IterableHelper.select(list01, handle01):
    print(item)

for item in IterableHelper.select(list01, lambda item: item.name):
    print(item)


# ---------------------练习2-----------------------------
# 1.定义函数，在老婆列表中累加所有老婆的总身高
"""
def sum01():
    sum_value = 0
    for item in list01:
        sum_value += item.height
    return sum_value


def sum02():
    sum_value = 0
    for item in list01:
        sum_value += item.weight
    return sum_value


def handle01(item):
    return item.height


def handle02(item):
    return item.weight


def sum(func):
    sum_value = 0
    for item in list01:
        # sum_value += item.weight
        # sum_value += handle02(item)
        sum_value += func(item)
    return sum_value
"""

# re = IterableHelper.sum(list01, lambda item: item.height)
# print(re)
