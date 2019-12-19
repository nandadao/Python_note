# 练习：定义函数,根据年月日计算星期（星期一、星期二、）
import time


def get_week(year, month, day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    list_weeks = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    index = tuple_time[6]
    return list_weeks[index]


print(get_week(2019, 11, 19))
