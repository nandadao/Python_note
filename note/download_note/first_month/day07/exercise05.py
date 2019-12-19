"""
    [5,56,65,7,87,3,9]
    升序(小 -->  大)
    思想：
        取出前几个(不要最后一个)
        依次与后面进行比较
        如果发现更小的则交换
"""
list01 = [5, 56, 65, 7, 87, 3, 9]
# # list01[0]
# # list01[1] list01[2] .. list[..]
# for i in range(1, len(list01)):
#     # list01[0]  list01[i]
#     pass
#
# # list01[1]
# # list01[2] list01[3] .. list[..]
# for i in range(2, len(list01)):
#     # list01[1]  list01[i]
#     pass

# 让列表中所有元素，俩俩比较。
# 取数据
for r in range(len(list01)-1):#0 1 2 3...len-2
    # 做比较
    for c in range(r+1, len(list01)):
        if list01[r] > list01[c]:
            list01[r],list01[c] = list01[c],list01[r]
print(list01)