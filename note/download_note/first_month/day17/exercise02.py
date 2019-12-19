"""
    练习：定义函数，获取全局变量list01中所有偶数
        使用传统思想 -- 使用容器存储所有结果
        使用生成器思想 -- 使用yield返回结果
        要求：调试，体会差异性。
        函数何时使用yield  return 返回结果？
                  多个     单个
"""

list01 = [4, 45, 5, 6, 76, 87, 8]


def get_even01():
    list_result = []
    for item in list01:
        if item % 2 == 0:
            list_result.append(item)
    return list_result


def get_even02():
    for item in list01:
        if item % 2 == 0:
            yield item


re = get_even01()
for item in re:
    print(item)

re = get_even02()
for item in re:
    print(item)
