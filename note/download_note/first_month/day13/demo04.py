"""
    运算符重载
"""

class Vector1:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return "向量的分量是：" + str(self.x)

    # +  (习惯创建新对象)
    def __add__(self, other):
        return Vector1(self.x + other.x)

    # += (习惯在原有对象基础上进行修改)
    def __iadd__(self, other):
        self.x += other.x
        return self

    # # 定义当前类对象的比较依据
    # def __eq__(self, other):
    #     return self.x  ==  other.x

# 1. 重写算数运算符
v01 = Vector1(10)
v02 = Vector1(20)
re = v01 + v02  # v01.__add__(v02)
print(re)
# 2. 重写增强运算符
print(id(v01))
v01 += Vector1(20)  # v01.__iadd__(Vector1(20))
print(id(v01))
print(v01)

# 3.
v03 = Vector1(10)
v04 = Vector1(10)
print(v03 == v04)  # v03.__eq__(v03)
list01 = [
    Vector1(10),
    Vector1(20),
    Vector1(30),
    Vector1(40),
]
print(Vector1(10) in list01)
print(list01.count(Vector1(10)))

# is
print(v03 is v04)# False

list01 = [1]
list02 = [1]
print(list01 == list02)# ? true    判断内容 list01.__eq__(list02)
print(list01 is list02)# ? false   判断地址 id(list01) == id(list02)



# 练习:随意重写2个其他算数运算符。
# 练习:随意重写2个其他增强运算符。
"""
list01 = [1]
print(id(list01))# 140200259532872
list01 += [2]
print(id(list01))# 140200259532872
print(list01)# [1,2]

list02 = [3]
print(id(list02))# 140599268399880
list02 = list02 + [4]
print(id(list02))#140599237579592
print(list02)
"""
