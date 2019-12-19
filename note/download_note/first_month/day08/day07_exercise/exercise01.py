"""
3. (扩展)根据图中算法，对方阵进行转置(不用函数)
"""
list01 = [
    [1, 2, 3, 4,"a"],
    [5, 6, 7, 8,"b"],
    [9, 10, 11, 12,"c"],
    [13, 14, 15, 16,"d"],
    [17, 18, 19, 20,"e"],
]
"""
# list01[1][0]  list01[0][1]
# list01[2][0]  list01[0][2]
# list01[3][0]  list01[0][3]
for r in range(1, 4):
    # list01[r][0] list01[0][r]
    pass
# list01[2][1]  list01[1][2]
# list01[3][1]  list01[1][3]
for r in range(2, 4):
    # list01[r][1] list01[1][r]
    pass

for c in range(1, 4):
    for r in range(c, 4):
        # list01[r][c-1] list01[c-1][r]
        pass
"""

for c in range(1, len(list01)):
    for r in range(c, len(list01)):
        list01[r][c - 1], list01[c - 1][r] = list01[c - 1][r], list01[r][c - 1]

print(list01)
