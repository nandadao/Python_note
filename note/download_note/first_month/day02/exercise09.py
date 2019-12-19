# 练习1：说出结论：
print(1 > 2 or 3 == 5)# False
print("a" != "b" and "10" != "10")# False
print(1.5 < 0.5 or 10 > 15.5)# False

# 练习2:
# 在终端中录入一个年份，判断是否为润年,打印True,False
# 条件：年份能被4整除，但是不能被100整除
#      年份能被400整除
year = int(input("请输入年份："))
result = year % 4 == 0  and  year % 100 != 0 or year % 400 == 0
print(result)