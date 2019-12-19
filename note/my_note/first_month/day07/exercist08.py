""
"""
# 练习:在终端中录入一个多位整数：1234
#     计算每位相加和. 1+2+3+4 --> 10
# 将下列代码定义到函数中
str_number = input("请输入整数：")
sum_value = 0
for item in str_number:
    sum_value += int(item)
print(sum_value)
"""


def numbers_sum(numbers):
    sum_1 = 0
    for i in numbers:
        sum_1 += int(i)
    return sum_1



# -------------------------------
str_number = input("请输入整数：")
re = numbers_sum(str_number)
print(re)









