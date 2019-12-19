""""""

"""
    矩阵：
        将list01 的每列，存储到list02的每行

        
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],

]

# list01[0][0]
# list01[1][0]
# list01[2][0]
# list01[3][0]

list02 = []
for c in range(4):
    line = []
    for r in range(4):
        line.append(list01[r][c])
    list02.append(line)

print(list02)

# for i in range(len(list01)):
#     for r in range(len(list01[i])):
#         list03.append(list01[i][r])
#     list02.append(list03)
# print(list02)
















