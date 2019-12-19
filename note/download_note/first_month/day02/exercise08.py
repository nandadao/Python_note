# 练习:在终端中录入一个四位整数：1234
#     计算每位相加和. 1+2+3+4 --> 10
number = int(input("请输入四位整数："))
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000
print("结果是：" + str(result))
