""
"""
        3.{扩展}   （4 * 4）
        保持对角线不变，交换对角线的两侧的数字
        list[1][0]  --->  list[0][1]
        list[2][0]  --->  list[0][2]
        ...
        方阵转置，（不用做成函数）
"""
list01 = [
    [1, 2, 3, 4 ,"a"],
    [5, 6, 7, 8 , "b"],
    [9, 10,11,12, "c"],
    [13,14,15,16, "d"],
    [2, 3, 4, 5, "e"]
]

# 保持对角线不变，交换对角线的两侧数字
for r in range(0, len(list01)-1):
    for c in range(r+1, len(list01[r])):
        list01[r][c], list01[c][r] = list01[c][r], list01[r][c]

# 以表格的形式打印出来
for r in range(len(list01)):
    for c in range(len(list01[r])):
        print(list01[r][c], end="\t")
    print()

# 结果如下
# # list01 = [
# #     [1, 5, 9,  13],
# #     [2, 6, 10, 14],
# #     [3, 7, 11, 15],
# #     [4, 8, 12, 16]
# # ]


"""
      4.定义函数，将二维列表 [[], [], []]，
      以表格状打印在终端中  
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# for r in range(len(list01)):
#     for c in range(len(list01[r])):
#         print(list01[r][c], end="\t")
#     print()

# def print_double_list(list_target):
#     for line in list_target:
#         for item in line:
#             print(item, end="\t")
#         print()
#
# print_double_list(list01)
"""
5.将下列代码转成函数，季度转月份，（输出数字）
    if season == "春天":
        print("1月2月3月")
    elif season == "夏天":
        print("4月5月6月")
    elif season == "秋天":
        print("7月8月9月")
    elif season == "冬天":
        print("10月11月12月")
"""

# # 代码实现
# def make_season_to_month(season):
#     if season == "春天":
#         return (1, 2, 3)
#     if season == "夏天":
#         return (4, 5, 6)
#     if season == "秋天":
#         return (7, 8, 9)
#     if season == "冬天":
#         return (10, 11, 12)
#     return "输入有误"
#
#
# # ----------------------------
# # 调用
# re = make_season_to_month("冬")
# print(re)

"""
6.定义函数，在列表中查找    最大值。
for r in range(len(list01)-1):
                                            # list[0][r]
                                            # list01[r+1]  list01[2]
                                            # 做比较
    for c in range(r+1, len(list01)):
        if list01[r]  > list01[c]:
            list01[r], list01[c]  = list01[c], list01[r]
print(list01)
"""


# # 集成函数
# def find_the_max(the_list):
#     for r in range(len(the_list) - 1):
#         for c in range(r + 1, len(the_list)):
#             if the_list[r] > the_list[c]:
#                 the_list[r], the_list[c] = the_list[c], the_list[r]
#
#     return the_list

# def get_max(list_target):
#     max_value = list_target[0]
#     for i in range(1, len(list_target)):
#         if max_value < list_target[i]:
#             max_value = list_target[i]
#     return max_value
#
#
# # ---------------------------------
# # 实现
# re = get_max([1, 4, 3, 2])
# print(re)
