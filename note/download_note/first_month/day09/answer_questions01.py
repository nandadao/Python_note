# 1. 结论:默认参数不要使用可变对象
def fun01(p1=[]):  # 将函数加载到代码区时,创建列表对象.
    p1.append(1)
    print(p1)


# 函数调用三次,使用的都是一个默认参数(列表)
fun01()  # [1]
fun01()  # [1, 1]
fun01()  # [1, 1, 1]


# 2.
def square_matrix_transposition(list_matrix):
    for c in range(1, len(list_matrix)):
        for r in range(c, len(list_matrix)):
            list_matrix[r][c - 1], list_matrix[c - 1][r] = list_matrix[c - 1][r], list_matrix[r][c - 1]


def matrix_transposition(list_matrix):
    result = []
    for c in range(4):
        line = []
        for r in range(4):
            line.append(list_matrix[r][c])
        result.append(line)
    return result


# 3.
for item in range(1, 10, 2):  # 1 3 5 7 9
    print(item)

for item in "123456789"[1:10:2]:  # 2 4 6 8
    print(item)


# 4. 局部变量何时销毁?
#   局部变量随栈帧销毁
#   指向的对象随引用计数
def fun02(p1):
    a = p1


g01 = [10, 20, 30]
fun02(g01)
