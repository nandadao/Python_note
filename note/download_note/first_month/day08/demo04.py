"""
    函数参数
        形式参数
            默认:可以不传参
            位置:必须传参
                星号元组:位置实参数量无限
            命名关键字:要求实参必须是关键字
                双号字典:关键字实参数量无限

    练习:exercise04
    练习:exercise05
    练习:exercise06
"""


# 1. 默认参数:实参可以不传递
#  (必须从又向左依次存在)
def fun01(p1="", p2=0, p3=0.0):
    print(p1)
    print(p2)
    print(p3)


fun01()
fun01("悟空", 10, 5.6)
# 关键字实参 + 默认参数:实参可以随意传递
fun01(p2=100)


# 2. 位置形参:实参必须传递
def fun02(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 3. 星号元组形参:使用星号将实参合并为一个元组
#   作用: 位置实参数量无限
#   备注:只能有一个
def fun03(*args):
    print(args)


fun03()
fun03(4, 54, 5, 65, 6)


# fun03(a=1, b=2, c=3) # 报错

# 4. 命名关键字形参:星号元组形参后面的参数
#   要求实参必须是关键字实参.
def fun04(*args, a, b=0):
    print(args)
    print(a)
    print(b)


fun04(34, 45, 54, 56, 67, 87, a=1, b=2)
fun04(34, 45, 54, 56, 67, 87, a=1)

# 4. 命名关键字形参:星号后面的参数
#   要求实参必须是关键字实参.
def fun05(a, *, b=0, c=""):
    print(a)
    print(b)

fun05(5,b = 6,c = 7)
fun05(5,c = 7)

# print(*args, sep=' ', end='\n', file=None)
print(3,4,54,5,56,end = " ")
print(3,4,54,5,56,sep = "-",end = " ")
# print(3,4,54,5,56,"-"," ")

# 5. 双星号字典形参:关键字实参数量无限
def fun05(**kwargs):
    print(kwargs)

fun05(a = 1,b = 2,c = 3)









