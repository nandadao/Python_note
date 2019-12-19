# 练习:在列表中找出最大元素.(不使用max)
# [23,4,345,5,546,67,67,78]
list01 = [23, 4, 345, 5, 546, 67, 67, 78]
# 1. 假设第一个就是最大值
max_value = list01[0]
# 2. 与后面元素进行比较
for i in range(1, len(list01)):  # 1 2 3.. len -1
    # 3. 发现更大的
    if max_value < list01[i]:
        max_value = list01[i]

print(max_value)
