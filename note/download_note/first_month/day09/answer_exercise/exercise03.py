"""
    定义函数，返回字符串中第一个不重复的字符。
    输入：ABCACDBEFD
    输出：E
"""


def get_repeating_info(target):
    dict_repeat_info = {}
    for char in target:
        dict_repeat_info[char] = target.count(char)
    # if char not in dict_repeat_info:
    #     dict_repeat_info[char] = 1
    # else:
    #     dict_repeat_info[char] += 1
    return dict_repeat_info


def get_key_for_value(target, value):
    for k, v in target.items():
        if v == value:
            return k


def first_not_repeating_char(target):
    dict_info = get_repeating_info(target)
    return get_key_for_value(dict_info, 1)


print(first_not_repeating_char("ABCACDBEFD"))
