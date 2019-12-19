"""
    定义函数，返回列表中不重复的元素(顺序不重要)。
    输入：[4,35,7,64,7,35]
    输出：[4, 35, 7, 64]
"""


def get_not_repeating(target):
    """
        获取不重复的元素
    :param target: list类型，表示具有重复元素的数据
    :return:
    """
    # return list(set(target))
    return list(dict().fromkeys(target).keys())


list01 = [4, 35, 7, 64, 7, 35]
print(get_not_repeating(list01))


