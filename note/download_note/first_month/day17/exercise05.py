# 练习: 获取list01中所有大于10整数
# 使用生成器函数与生成器表达式实现
# 15:20
list01 = [11, 2, "a", True, 33]


def get_number():
    for item in list01:
        if type(item) == int and item > 10:
            yield item


for item in get_number():
    print(item)

for item in (item for item in list01 if type(item) == int and item > 10):
    print(item)
