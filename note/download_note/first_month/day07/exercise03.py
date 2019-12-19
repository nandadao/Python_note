
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# 1. 打印二维列表第三行数据(一行一个)
for item in list01[2]:
    print(item)
# 2. 打印二维列表第二列数据(一行一个)
# print(list01[0][1])
# print(list01[1][1])
# print(list01[2][1])
# print(list01[3][1])
# 0 -- 3
for r in range(len(list01)):
    print(list01[r][1])
# 3. 打印二维列表所有数据(表格状)
for line in list01:
    for item in line:
        print(item, end="\t")
    print()
# 4. 从下到上打印第三列数据(一行一个)
# print(list01[3][2])
# print(list01[2][2])
# print(list01[1][2])
# print(list01[0][2])
for r in range(3, -1, -1):
    print(list01[r][2])
# 5. 从右到左打印第四行数据(一行一个)
for c in range(3, -1, -1):
    print(list01[3][c], end=" ")
