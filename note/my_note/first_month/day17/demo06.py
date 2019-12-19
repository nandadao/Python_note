"""
    函数式编程---应用
"""

list01 = [3, 4, "a", "b", 80]
# 需求一：定义函数：获取列表中所有字符串
def find02():
    for item in list01:
        if type(item) == str:
            yield item

# 需求二：定义函数，获取列表中所有大于10的整数


# "封装"  --- 分变化点
def condition01(item):
    return type(item) == str

def condition02(item):
    return type(item) == int and item > 10

# 提取共性
# 万能查找
def find(target,func):
    for item in target:
        if func(item):
            yield item

# "继承" --- 隔(抽象 -- 统一)
# "多态"  --- (重写)
for i in find(list01, condition02):
    print(i)















