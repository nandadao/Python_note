# 6. 定义函数,在列表中查找最大值。
def get_max(list_target):
    max_value = list_target[0]
    for i in range(1, len(list_target)):
        if max_value < list_target[i]:
            max_value = list_target[i]
    return max_value


list01 = [5, 4, 657, 89, 56]
result = get_max(list01)
print(result)
