"""
    内置高阶函数
"""
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


# 1.在老婆列表中查找，所有体重大于160的老婆对象
# for item in IterableHelper.find_all(list01, lambda element:element.weight > 160):
#     print(item)

# filter过滤器
for item in filter(lambda element:element.weight > 160, list01):
    print(item)

# 2.查找姓名体重
# for item in IterableHelper.select(list01, lambda e:(e.name, e.weight)):
#     print(item)

# map 映射
for item in map(lambda e:(e.name, e.weight), list01):
    print(item)

# 3.在老婆列表中体重最大的
# re = IterableHelper.get_max(list01, lambda e:e.weight)

re = max(list01, key= lambda e:e.weight)
print(re)

# 4.排序
# IterableHelper.order_by_small_to_big(list01, lambda e:e.weight)

for item in sorted(list01, key= lambda e:e.weight, reverse=True):
    print(item)














