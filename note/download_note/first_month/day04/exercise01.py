# 练习:在终端中录入一个多位整数：1234
#     计算每位相加和. 1+2+3+4 --> 10
str_number = input("请输入整数：")
sum_value = 0
for item in str_number:
    sum_value += int(item)
print(sum_value)
