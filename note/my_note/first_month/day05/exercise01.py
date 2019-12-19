"""
    练习：
        [5, 6, 17, 34, 5]
            删除大于10的元素
        温馨提示：调试画图
"""
list01 = [5, 6, 17, 78, 34, 5]
# for i in list01:
#     if i > 10:
#         # list01.remove(i)

for i in range(len(list01)-1 , -1, -1):
    if list01[i] > 10:
        list01.remove(list01[i])
        


print(list01)

