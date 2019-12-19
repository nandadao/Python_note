"""
    练习：获取list01中所有大于10的整数
"""
list01 = [11, 2, "a", True, 33]

# 生成器函数(写完后，给别人用)


def get_bigger_than_10():
    for item in list01:
        if type(item) is int and item > 10:
            yield item


for item in get_bigger_than_10():
    print(item)


# 生成器表达式
for item in (item for item in list01 if type(item) is int and item > 10 ):
    print(item)










