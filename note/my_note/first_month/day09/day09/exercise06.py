"""
    "水仙花数":各位数字立方和等于该数本身
    定义函数，根据位数计算水仙花数
    输入：3
    输出：[153, 370, 371, 407]
"""

def flowers_number(n):
    # count = 0
    for i in range(10**(n-1), 10**n):
        count = 0
        list01 = list(str(i))
        # print(list01)
        for j in range(n):
            count += int(list01[j])**n
        if count == i:
            print(count)

flowers_number(3)









