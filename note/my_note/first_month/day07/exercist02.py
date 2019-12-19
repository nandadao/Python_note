""
"""
    list01 = [
    ]
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],

]
# 1.打印二维列表，第三行数据（一行一个）

for item in list01[2]:
    print(item)


# for i in range(len(list01)):
#     for item in range(len(list01[i])):
#         print(list01[i][item], end=",")
#     print()

# for i in range(len(list01)):
#     if i == 2:
#         for item in list01[i]:
#             print(item)


# 2.打印二维列表，第二列数据（一行一个）

# for i in range(len(list01)):
#     print(list01[i][1])

# 3.打印二维列表所有数据（表格装，不要标点）
# for i in range(len(list01)):
#     for item in range(len(list01[i])):
#         print(list01[i][item], end="\t")
#     print()



# 4.从下到上打印第三列数据（一行一个）
# for i in range(len(list01)-1, -1, -1):
#     print(list01[i][2])

# 5.从右到左打印第四行数据（一行一个）

for item in range(len(list01[3])-1, -1, -1):

    print(list01[3][item], end=" ")



















