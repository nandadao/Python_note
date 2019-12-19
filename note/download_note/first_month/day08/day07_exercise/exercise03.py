"""
5. 将下列代码定义到函数中，根据季度获取月份的功能
    if season == "春天":
        print("1月2月3月")
    elif season == "夏天":
        print("4月5月6月")
    elif season == "秋天":
        print("7月8月9月")
    elif season == "冬天":
        print("10月11月12月")
"""


def get_month(str_season):
    if str_season == "春天":
        return (1, 2, 3)
    if str_season == "夏天":
        return (4, 5, 6)
    if str_season == "秋天":
        return (7, 8, 9)
    if str_season == "冬天":
        return (10, 11, 12)


tuple_month = get_month("春天")
print(tuple_month)
