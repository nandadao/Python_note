"""
   从小到大排列 （升序排列）
    思想：
        取出前几个（不要组后一个）
        一次与后面进行比较
        如果发现更小的则交换
"""

list01 = [5, 56, 65, 7, 87, 3, 9, 10, 5, 7]


# 自己写的
# 这是第一个
# for item in range(6):
#     for i in range(len(list01)-1):
#
#         if list01[i] > list01[i+1]:
#             list01[i], list01[i+1] = list01[i+1], list01[i]
# print(list01)


# 老师的  ×××××××× 重要
# 取数据
# 让列表中所有元素，俩俩比较
for r in range(len(list01)-1):
                                            # list[0][r]
                                            # list01[r+1]  list01[2]
                                            # 做比较
    for c in range(r+1, len(list01)):
        if list01[r]  > list01[c]:
            list01[r], list01[c]  = list01[c], list01[r]
print(list01)









