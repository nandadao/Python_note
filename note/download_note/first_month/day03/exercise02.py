"""
    在终端种录入一个季度，打印月份。
        春天 --> 1月2月3月
        夏天 --> 4月5月6月
        秋天 --> 7月8月9月
        冬天 --> 10月11月12月
"""
season = input("请输入季度：")
# if season == "春天":
#     print("1月2月3月")
# if season == "夏天":
#     print(" 4月5月6月")
# if season == "秋天":
#     print("7月8月9月")
# if season == "冬天":
#     print("10月11月12月")

# 如果前面条件满足，后面条件不再判断。
if season == "春天":
    print("1月2月3月")
elif season == "夏天":
    print(" 4月5月6月")
elif season == "秋天":
    print("7月8月9月")
elif season == "冬天":
    print("10月11月12月")
