"""
    时间模块
"""
import time

# 1.时间戳(1970年1月1日到现在经过的秒数)
print(time.time())

# 2.时间元组(年月日十分秒星期， 年的天，夏令时偏移量)
print(time.localtime())
tuple_tiem = time.localtime()
print(tuple_tiem[3:6])   # 输出十分秒

# 3.时间戳----> 时间元组
print(time.localtime(157153741.733721))

# 4.时间元组  -- > 时间戳
print(time.mktime(tuple_tiem))

# 5.时间元组 -- > 字符串
# "2019年11月19日"
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒",tuple_tiem))

# 6.字符串 --> 时间元组
print(time.strptime("2019年11月19日 17时08分48秒","%Y年%m月%d日 %H时%M分%S秒"))




