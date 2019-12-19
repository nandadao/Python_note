# 练习:定义函数,多个数值累加.
# def sum_numbers(list_target):
#     sum_value = 0
#     for item in list_target:
#         sum_value += item
#     return sum_value
#
# print(sum_numbers([54,54,56,6,76,8]))

def sum_numbers(*args):
    sum_value = 0
    for item in args:
        sum_value += item
    return sum_value


print(sum_numbers(54, 54, 56, 6,5))
