# 练习:在终端中录入一个四位整数：1234
#     计算每位相加和. 1+2+3+4 --> 10
number = int(input("请输入四位整数："))
# 1234 % 10 --> 4
unit01 = number % 10
# 1234 // 10  --> 123 % 10 --> 3
unit02 = number // 10  % 10
# 1234 // 100 --> 12 % 10 --> 2
unit03 = number // 100  % 10
# 1234 // 1000 --> 1
unit04 = number // 1000
result = unit01 + unit02 + unit03 + unit04
print("结果是："+str(result))

