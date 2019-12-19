"""
    练习:
    在列表中[5,6,17,78,34,5]
    删除大于10的元素
    温馨提示：调试/画图
"""
list01 = [5, 6, 17, 78, 34, 5]
# for item in list01:
#     if item > 10:
#         # 删除的是变量
#         # del item
#         # 漏删(后面元素向前移动)
#         list01.remove(item)

# for i in range(len(list01)):
#     if list01[i] > 10:
#         # 错误(删除元素则总数减少)
#         del list01[i]#

# 解决：倒序删除
for i in range(len(list01) - 1, -1, -1):
    if list01[i] > 10:
        del list01[i]

print(list01)
