# 练习:在终端中录入一个月份，打印天数。
#  1 3 5 7 8 10 12  -->  31天
#  2 --> 28天
#  4 6 9 11  --> 30天
#  月份有误
# 15:13
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("月份有误")
elif month == 2:
    print("28天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30天")
else:  # 1 3 5 7 8 10 12
    print("31天")
