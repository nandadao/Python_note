"""
    练习：
        定义函数，在老婆列表中查找所有年龄大于25的老婆对象
        定义函数，在老婆列表中查找所有身高小于180的老婆对象

"""

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
    Wife("大乔", 165, 44, 28),
    Wife("小乔", 176, 88, 19),
    Wife("貂蝉", 170, 55, 26),
    Wife("王昭君", 176, 88, 31),
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
    return item.height < 180

# 万能查找
# find 第一个参数： 数据
# find 第二个参数： 逻辑
# 万能：数据以及对数据的核心操作，都是灵活的
def find(target, func):
    for item in target:
        if func(item):
            yield item

for item in find(list01, condition01):
    print(item)













