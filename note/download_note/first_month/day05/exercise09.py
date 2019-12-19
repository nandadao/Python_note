# 练习:根据月日，计算是这一年的第几天。
# 3 月 5 日
# 31 + 28 + 5

month = int(input("请输入月份："))
day = int(input("请输入天："))

# 将每月天数存储元组
days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# 3 --> 1  --> 2
# days_of_month[0]  days_of_month[1]
# 5 --> 3  --> 4
# days_of_month[0]  days_of_month[1]   days_of_month[2]    days_of_month[3]
# 传统思想：
# total_day = day
# for i in range(month - 1):
#     total_day += days_of_month[i]
total_day = sum(days_of_month[:month - 1])
total_day += day
print(total_day)

