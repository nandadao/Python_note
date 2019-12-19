
# 升序排列
list_01 = [1, 2, 22, 1, 2, 3]
for r in range(len(list_01)-1):
    for c in range(r+1, len(list_01)):
        if list_01[r] > list_01[c]:
            list_01[r], list_01[c] = list_01[c], list_01[r]


print(list_01)



























