"""
4. 定义函数,将二维列表，以表格状打印在终端中。
"""

def print_double_list(list_target):
    """
        在终端中打印二维列表
    :param list_target:需要打印的数据
    """
    for line in list_target:
        for item in line:
            print(item,end = "\t")
        print()

list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

print_double_list(list01)
print_double_list(list01)




