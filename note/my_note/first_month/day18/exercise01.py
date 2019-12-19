
# 1.定义函数，在老婆列表中查找所有老婆的姓名
# 2.定义函数，在老婆列表中查找所有老婆的姓名和身高
# 步骤：
#     1.将需求完整实现到函数中
# 2.将变化点单独定义到函数中
# 3.将通用代码定义到函数中
# 4.用餐数隔离变化点
# 5.将通过代码移动到IterableHelper类中
# 6.测试调用IterableHelper的静态方法执行功能。
from common.tools import IterableHelper


class Wife:
    """
        抽象的数据 模型
    """
    def __init__(self, name="", height=0, weight=0, age=0):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def __str__(self):
        return "%s--%d--%d--%d"%(self.name, self.age,self.weight,self.height)

list01= [
    Wife("大乔", 165, 166, 28),
    Wife("小乔", 176, 89, 21),
    Wife("貂蝉", 170, 188, 26),
    Wife("王昭君", 177, 88, 31),
 ]

# 年龄大于25
def find01(list_target):
    for item in list_target:
        if item.age > 25:
            yield item

# 身高小于180
def find02(list_target):
    for item in list_target:
        if item.height < 180:
            yield item

# 封装变化点
def condition01(item):
    return item.age > 25
def condition02(item):
    return item.height < 1



# for item in IterableHelper.find_all(list01, condition01):
#     print(item)

# 1.定义函数，在老婆列表中查找所有老婆的姓名
# 2.定义函数，在老婆列表中查找所有老婆的姓名和身高
# 步骤：
#     1.将需求完整实现到函数中
# 2.将变化点单独定义到函数中
# 3.将通用代码定义到函数中
# 4.用餐数隔离变化点
# 5.将通过代码移动到IterableHelper类中
# 6.测试调用IterableHelper的静态方法执行功能。

# ---------------------------------
# 练习1
def select01():
    for item in list01:
        yield item.name

def select02():
    for item in list01:
        yield (item.name, item.height)

def handle01(item):
    return item.name
def handle02(item):
    return (item.name,item.height)

def select0():
    for item in list01:
        yield handle02(item)
for item in select0():
    print(item)

def select(func):
    for item in list01:
        yield func(item)

# for item in IterableHelper.select(list01, handle01):
#     print(item)


# 1.定义函数，在老婆列表中所有老婆的总的身高
# 2.定义函数，在老婆列表中累加所有老婆的总体总

def add_height():
    height_total = 0
    for item in list01:
        height_total += item.height
    return height_total

# re = add_height()
# print(re)

def add_weight():
    weight_total = 0
    for item in list01:
        weight_total += item.weight
    return weight_total

def change01(item):
    return item.height
def change02(item):
    return item.weight


def add_func(iterable, change):
    total = 0
    for item in iterable:
        total += change(item)
    return total

# re = IterableHelper.add_func(list01, lambda item:item.height)
# print(re)



# 1.定义函数，在老婆列表中所删除年龄在20-25之间的
# 2.定义函数，在老婆列表中删除体重大于160的

# list01= [
#     Wife("大乔", 165, 166, 28),
#     Wife("小乔", 176, 88, 20),
#     Wife("貂蝉", 170, 188, 26),
#     Wife("王昭君", 176, 88, 31),
#  ]

print("--------------------------")
def delete_age():
    for i in range(len(list01)-1, -1, -1):
        if 20 <= list01[i].age <= 25:
            del list01[i]

# delete_age()
# for item in list01:
#     print(item)


def delete_height():
    for i in range(len(list01)-1, -1, -1):
        if 20 <= list01[i].age <=25:
            del list01[i]

# def delete(iterate, handle_func):
#     for i in range(len(iterate)-1, -1, -1):
#         if handle_func:
#             iterate.remove()


#---------------------------练习3
# re = IterableHelper.delete_all(list01, lambda item:20<= item.age <=25)
# print(re)
#
# re = IterableHelper.delete_all(list01, lambda element:element.weight > 160)
# print(re)


# ----------------------------------
# 直接做第五步和第六步骤
# 1.在老婆列表中找出年龄最大的老婆
# 2.在老婆列表中找出身高最高的老婆

print("======================")
# re = IterableHelper.get_max(list01, lambda item:item.weight)
# print(re)

#----------------------------第四个练习

# 1.定义函数，根据体重对老婆列表进行升序排序
# 2.身高排序

print("排序")

# IterableHelper.order_by(list01, lambda item:item.height)
# for item in list01:
#     print(item)







