"""
    定义函数，判断二维数字列表中是否存在某个数字
    输入：二维列表、11
    输出：True
"""

list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]


def is_exists(double_list, target):
    """
        判断二维列表中是否存在指定元素
    :param double_list:list类型，表示二维列表
    :param target:需要判断的元素
    :return:bool类型，是否存在。
    """
    for line in double_list:
        if target in line:
            return True
    return False


print(is_exists(list01, 18))
