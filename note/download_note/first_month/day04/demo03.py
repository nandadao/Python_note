"""
    continue
    练习：exercise04
"""
# 累加1--100之间整数,能被3整除的数字。
sum_value = 0
# for item in range(1,101):
#     # 能被3整除 累加
#     if item % 3 == 0:
#         sum_value += item

for item in range(1,101):
    # 不能 能被3整除 跳过
    if item % 3 != 0:
        continue# 继续下次循环
    sum_value += item
print(sum_value)

