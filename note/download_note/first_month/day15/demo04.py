"""
    标准库模块
        time 时间
    练习:exercise02/03
"""
import time

# 1. 当前时间戳（1970年1月1日到现在经过的秒数）
print(time.time())  # 1574153197.3360288
# 2. 时间元组(年,月,日,时,分,秒,星期,年的天,夏令时偏移量)
tuple_time = time.localtime()
print(tuple_time)
print(tuple_time[1])
print(tuple_time[3:6])
# 3. 时间戳 --> 时间元组
print(time.localtime(1153197.3360288))
# 4. 时间元组-->时间戳
print(time.mktime(tuple_time))
# 5. 时间元组--> 字符串
print(time.strftime("%Y年%m月%d日 %H小时%M分钟%S秒", tuple_time))
# 6.字符串 -->  时间元组
print(time.strptime("2019-11-19 17:10:13", "%Y-%m-%d %H:%M:%S"))
