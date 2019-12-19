"""
根据季度，打印月份
    if season == "春天":
        print("1月2月3月")
    elif season == "夏天":
        print(" 4月5月6月")
    elif season == "秋天":
        print("7月8月9月")
    elif season == "冬天":
        print("10月11月12月")
    else:
        print("季度有误")
"""
dict_season = {
    "春天": "1月2月3月",
    "秋天": "4月5月6月",
    "夏天": "7月8月9月",
    "冬天": "10月11月12月",
}
season = input("请输入季节：")
if season in dict_season:
    print(dict_season[season])
else:
    print("季度有误")

