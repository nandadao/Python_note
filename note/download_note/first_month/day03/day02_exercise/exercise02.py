"""
   1. 在终端中录入小时数，分钟数，秒数，计算总共的秒数.
   2. 在终端中录入总秒数，计算几小时零几分钟数零秒数。
"""
# 1.
# hour = int(input("请输入小时："))
# minute = int(input("请输入分钟："))
# second = int(input("请输入秒："))
# result = hour * 60 * 60 + minute * 60 + second
# print("总秒数是：" + str(result))

# 2.
total_second = int(input("请输入总秒数："))
hour = total_second // 60 // 60
second = total_second % 60
minute = total_second // 60  % 60
print(hour)
print(minute)
print(second)