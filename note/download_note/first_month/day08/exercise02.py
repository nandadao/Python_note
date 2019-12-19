"""
    将下列代码，定义到函数中。
"""

# 排序:day07/exercies05
# for r in range(len(list01)-1):#0 1 2 3...len-2
#     # 做比较
#     for c in range(r+1, len(list01)):
#         if list01[r] > list01[c]:
#             list01[r],list01[c] = list01[c],list01[r]
# print(list01)

# 满足以下两个条件，不要用返回值。
# 1. 传入可变对象
# 2. 修改可变对象
def sort(list_target):
    for r in range(len(list_target) - 1):
        # 做比较
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    return list_target


list01 = [4, 54, 65, 7, 8, 9]
# re = sort(list01)
# print(re)
sort(list01)
print(list01)


# 方阵转置：day08/day07_exercise/exercise01
# for c in range(1, len(list01)):
#     for r in range(c, len(list01)):
#         list01[r][c - 1], list01[c - 1][r] = list01[c - 1][r], list01[r][c - 1]

def square_matrix_transposition(list_matrix):
    for c in range(1, len(list_matrix)):
        for r in range(c, len(list_matrix)):
            list_matrix[r][c - 1], list_matrix[c - 1][r] = list_matrix[c - 1][r], list_matrix[r][c - 1]


list01 = [
    [1, 2, 3, 4, "a"],
    [5, 6, 7, 8, "b"],
    [9, 10, 11, 12, "c"],
    [13, 14, 15, 16, "d"],
    [17, 18, 19, 20, "e"],
]
# 矩阵转置的转置等于原矩阵
square_matrix_transposition(list01)
square_matrix_transposition(list01)
print(list01)


def matrix_transposition(list_matrix):
    result = []
    for c in range(4):
        line = []
        for r in range(4):
            line.append(list_matrix[r][c])
        result.append(line)
    return result


re = matrix_transposition(list01)
print(re)
