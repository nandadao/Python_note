# 练习：循环将季度转换为月份，如果输入q则退出.
while True:
    season = input("请输入季度：")
    if season == "春天":
        print("1月2月3月")
    elif season == "夏天":
        print(" 4月5月6月")
    elif season == "秋天":
        print("7月8月9月")
    elif season == "冬天":
        print("10月11月12月")
    if input("请输入q退出") == "q":
        break
