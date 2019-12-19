"""
    练习：
        把打印矩形定义成函数
"""

def print_juxing(h, l, char):
    """
        打印矩形
    :param h: int
    :param l: int
    :return:
    """
    for r in range(h):
        for c in range(l):
            print(char, end=" ")
        print()

print_juxing(4, 5, "$")





















