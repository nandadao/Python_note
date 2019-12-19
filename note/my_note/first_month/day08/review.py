list01 = [1, 8, 9, 2, 3, 5, 6, 8]

# 思路：从头选取一个数字，然后，再选取一个，两者之间进行比较，如果大于就互换位置
# 把大的放在后面

for r in range(len(list01) -1):
    for c in range(r+1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c]  = list01[c], list01[r]
print(list01)











