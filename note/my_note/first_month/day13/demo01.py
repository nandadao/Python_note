



class Vector1:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return str(self.x)


    #
    def __add__(self, other):
        return Vector1(self.x + other.x)

    def __isub__(self, other):
        self.x -= other.x
        return self

    def __itruediv__(self, other):
        self.x /= other.x
        return self

    # 定义当前类对象的比较依据
    def __eq__(self, other):
        return self.x == other.x


# v01 = Vector1(10)
# v02 = Vector1(20)
#
# re = v01 + v02 # v01.__add__(v02)
# print(re)
#
# # print(id(v01))
# # v01 -= v02
# # print(v01)
# # print(id(v01))
#
# v01 /= v02
# print(v01)


# 3.
v03 = Vector1(10)
v04 = Vector1(10)
print(v03 == v04)

list01 = [
    Vector1(10),
    Vector1(20),
    Vector1(30),
    Vector1(40),
]

print(Vector1(10) in list01)
print(list01.count(Vector1(10)))

# is 判断地址是否相等

print(v03 is v04)






