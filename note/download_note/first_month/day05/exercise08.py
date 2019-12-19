"""
    元组
"""
month = int(input("请输入月份："))
# if month < 1 or month > 12:
#     print("月份有误")
# elif month == 2:
#     print("28天")
# # elif month == 4 or month == 6 or month == 9 or month == 11:
# elif month in (4,6,9,11):
#     print("30天")
# else:
#     print("31天")

# 将每月天数存储元组
days_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
print(days_of_month[5-1])
