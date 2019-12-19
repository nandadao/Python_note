"""
    练习:
"""


def fun01(*args, **kwargs):
    print(args)
    print(kwargs)


# 位置实参无限, 关键字实参无限
fun01()
fun01(1, 2, a=1, b=2)
fun01(1, 2)
fun01(a=1, b=2)


# fun01(a = 1,10,b=2)

def fun02(a, b, *args, c=0, d=0, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


fun02(1, 2, c=3)
fun02(1, 2, 3, 4, 5, c=3, d=4, e=5)
