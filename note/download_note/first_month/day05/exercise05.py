# 练习1：使用列表推导式生成1--50之间，
#        能被3或者5整除的数字
list01 = [item for item in range(1, 51) if item % 3 == 0 or item % 5 == 0]
print(list01)

# 练习2：使用列表推导式生成5 -- 20之间数字的三次方
list02 = [item ** 3 for item in range(5, 21)]
print(list02)
# 15:20