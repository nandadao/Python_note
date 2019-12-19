"""
    练习
"""
# 经可能多的调用

# def fun01(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# # 位置实参无限，关键字实参无限
# fun01()  # (),{}
#
# fun01(1,2,3,4,a=1, b=2)
# fun01(a=1, b=2,)
# fun01(1, 2, 3)
# fun01(a= 1, b=3, 1, 2, 4)


# 按照正确的方式调用
def fun02(a, b, *args, c=0, d=0, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

# a, b位置的必须填写
# *args: 可以不填
# c=0, d=0:   c = ...,   d= ,,,
#  *kwargs : e=1, f=2

fun02(1, 2, 1,2,3,e=1, f=3)
fun02(1, 2, 1,2,3,c=1, d=5, e=1, f=3)
fun02(2, 3,1,c=1, d=3, e=1)









