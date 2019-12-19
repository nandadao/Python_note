"""
    函数返回值--应用
    练习:exercise09
"""
# 小而精
# 需求：两个数字相加的功能
def add(number_one, number_two):
    return number_one + number_two


# ------------------------------------
number_one = float(input("请输入第一个数字："))
number_two = float(input("请输入第二个数字："))
re = add(number_one, number_two)
print("结果是：" + str(re))
