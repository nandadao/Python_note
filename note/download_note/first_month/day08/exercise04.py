# 练习:定义函数,根据时分秒计算总秒数
#    根据时分 --> 总秒数
#    根据时秒 --> 总秒数
#    根据分秒 --> 总秒数
#    根据分 --> 总秒数

def get_total_second(hour=0, minute=0, second=0):
    return hour * 3600 + minute * 60 + second

print(get_total_second(1, 2, 3))
print(get_total_second(1, 2))
print(get_total_second(1, second=2))
print(get_total_second(minute=1, second=2))
print(get_total_second(minute=1))
