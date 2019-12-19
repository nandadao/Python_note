"""
    创建老婆(姓名，身高，体重，年龄)列表
        定义函数：在老婆列表中查找身高在160 -170 之间的所有老婆
        定义函数：在老婆列表中查找年龄在25 -- 30 之间的所有老婆姓名与年龄

    使用生成器函数，与生成器表达式

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



#     def list_return(self):
#         return [self.name, self.height, self.weight, self.age]
#
#     def __iter__(self):
#         pass
#
#
# list_wife = Wife("大乔", 165, 88, 28)
# Wife("小乔", 176, 88, 19)
# Wife("貂蝉", 170, 88, 26)
# Wife("王昭君", 176, 88, 31)


def find01(list_target):
    for item in list_target:
        if 160 <= item.height <= 170:
            yield item

# ------------------测试代码
list01= [
    Wife("大乔", 165, 44, 28),
    Wife("小乔", 176, 88, 19),
    Wife("貂蝉", 170, 55, 26),
    Wife("王昭君", 176, 88, 31),
 ]

# for item in find01(list01):
#     print(item)
#
# for item in (item for item in list01 if 160 <= item.height <= 170):
#     print(item)

# 练习2
def find02(list_target):
    for item in list_target:
        if 25 <= item.age <= 30:
            yield (item.name,item.age)

# 惰性操作/延迟操作
# 优点：节省内存
# 缺点：不能灵活访问，即不能使用索引、切片访问


# 惰性操作  --> 立即操作
# 优点：灵活访问，即能使用索引、切片访问
# 缺点：占用内存过多

# generate01 = find01(list01)
# print(list(generate01)[0])


# 定义函数，在老婆列表中查找“小乔”老婆对象
# 定义函数，查找体重在40--- 60

def find03(list_target):
    for item in list_target:
        if item.name == "小乔":
            return item

def find04(list_target):
    for item in list_target:
        if 40 <= item.weight <= 60:
            yield item


print(find03(list01))



# for item in find04(list01):
#     print(item)












# 自己写的代码

# # list_wife = [
# #     ["大乔", 165, 88, 28],
# #     ["小乔", 176, 88, 19],
# #     ["貂蝉", 170, 88, 26],
# #     ["王昭君", 176, 88, 31],
# # ]
#
# def height_wife():
#     for item in list_wife:
#         if 160 <= item[1] <= 170:
#             yield item
# # for item in height_wife():
# #     print(item)
# #
# # for item in (item for item in list_wife if 160 <= item[1] <= 170):
# #     print(item)
#
# def age_wife():
#     for item in list_wife:
#         if 25 <= item[3] <= 30:
#             yield item[0], item[3]
# for item in age_wife():
#     print(item)
# for item in (item for item in list_wife if 25 <= item[3] <= 30):
#     print(item)












