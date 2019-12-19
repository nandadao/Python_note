"""
    定义函数，将全局变量list01中所有偶数
        1.使用传统思想    ---  使用容器存储所有结果
        2.使用生成器思想  ----  使用yield返回结果
        3.调试体会差异性
"""
list01 = [1, 33, 55, 2, 7, 8]


# 1.使用容器思想
def find_ou(list_input):
    list_result = []
    for item in list_input:
        if item % 2 == 0:
            list_result.append(item)
    return list_result

re = find_ou(list01)
print(re)

# 2.使用生成器思想
def find_ou_yield(list_input):
    for item in list_input:
        if item % 2 == 0:
            yield item

# re = find_ou_yield(list01)
# for i in re:
#     print(i)









