"""
    根据季度，打印月份

"""

# 核心思想：
dict_jidu = {
    "春季":"1 2 3",
    "夏季":"4 5 6",
    "秋季":"7 8 9",
    "冬季":"10 11 12"
}
while True:
    your = input("请输入季度：")
    if your in dict_jidu:
        print(dict_jidu[your])
    else:
        print("输入有误")

