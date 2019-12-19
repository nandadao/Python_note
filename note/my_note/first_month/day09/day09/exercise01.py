"""
    定义函数，返回列表中不重复的元素(顺序不重要)。
    输入：[4,35,7,64,7,35]
    输出：[4, 35, 7, 64]
"""

list01 = [4, 35, 7, 64, 7, 35, 4, 2]


def remove_same(list_input):
    list_input = list(set(list_input))
    return list_input


re = remove_same(list01)
print(re)
