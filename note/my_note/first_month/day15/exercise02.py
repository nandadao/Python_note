"""
    定义函数：
        根据年月日 计算  星期（星期一、星期二。。。）
"""
import time

def change_time(year, month, day):

    tuple_time = time.strptime("%d-%d-%d"%(year,month,day), "%Y-%m-%d")  # 这是时间元组
    list_week = ["星期一", "星期二", "星期三", "星期四", "星期五"]
    index = tuple_time[6]
    return list_week[index]

# print(change_time(2019, 11, 19))

# 练习2：定义函数，根据生日(年月日)计算活了多少天
# 公式：现在时间 - 出生时间

def count_live_days(year, month, day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    time_live = time.time() - time.mktime(tuple_time)
    days = time_live // (24*60*60)
    return days

re = count_live_days(2019, 11, 18)
print(re)



















