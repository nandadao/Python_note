# 排序
# for r in range(len(list01)-1):#0 1 2 3...len-2
#     # 做比较
#     for c in range(r+1, len(list01)):
#         if list01[r] > list01[c]:
#             list01[r],list01[c] = list01[c],list01[r]
# print(list01)


list01 = [1, 2, 6, 2, 4]

# 如果满足以下两个条件：不要用返回值
#  1.传入可变对象
#  2.修改可变对象
def small_to_big(list_target):
    for r in range(len(list_target) - 1):#0 1 2 3...len-2
        # 做比较
        for c in range(r+1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]


print(list01)




# # 方阵转置
# for c in range(1, len(list01)):
#     for r in range(c, len(list01)):
#         list01[r][c - 1], list01[c - 1][r] = list01[c - 1][r], list01[r][c - 1]
#
# print(list01)


list02 = [
    [1, 2, 3, 4,"a"],
    [5, 6, 7, 8,"b"],
    [9, 10, 11, 12,"c"],
    [13, 14, 15, 16,"d"],
    [17, 18, 19, 20,"e"],
]

def make_list(input_list):
    for c in range(1, len(input_list)):
        for r in range(c, len(input_list)):
            input_list[r][c - 1], input_list[c - 1][r] = input_list[c - 1][r], input_list[r][c - 1]


print(list02)
























