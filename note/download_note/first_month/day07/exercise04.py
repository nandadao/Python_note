"""
    矩阵转置
        将list01中的每列，存储到list02中的每行.
"""

list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

list02 = []
# print(list01[0][0])
# print(list01[1][0])
# print(list01[2][0])
# print(list01[3][0])

# line = []
# for r in range(4):
#     line.append(list01[r][0])
# list02.append(line)
#
# line = []
# for r in range(4):
#     line.append(list01[r][1])
# list02.append(line)
#
# line = []
# for r in range(4):
#     line.append(list01[r][2])
# list02.append(line)
#
# line = []
# for r in range(4):
#     line.append(list01[r][3])
# list02.append(line)

for c in range(4):
    line = []
    for r in range(4):
        line.append(list01[r][c])
    list02.append(line)

print(list02)
