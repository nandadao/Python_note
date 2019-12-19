# 练习1:在终端种录入一个整数，如果是奇数为变量state
#       赋值为"奇数"，否则赋值为偶数.
number = int(input("请输入整数："))
# if number % 2 ==1:
#     state = "奇数"
# else:
#     state = "偶数"

# if number % 2:
#     state = "奇数"
# else:
#     state = "偶数"

state = "奇数" if number % 2 else "偶数"
print(state)
# 练习2:在终端种录入一个年份，如果是润年为变量day
#       赋值为29，否则赋值为28.
year = int(input("请输入年份："))
# 不建议使用真值表达式
# if not year % 4 and year % 100 or not year % 400:
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     day = 29
# else:
#     day = 28
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
