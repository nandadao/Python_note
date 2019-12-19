"""
    定义函数，判断二维数字列表中是否存在某个数字
    输入：二维列表、11
    输出：True/False
"""
map = [
    [2, 0, 2, 0],
    [2, 4, 0, 2],
    [0, 0, 2, 0],
    [2, 4, 4, 11],
]
# print(2 in map)# False


def if_exist(list_two_weidu, num):
    for i in list_two_weidu:
        for j in i:
            if j == num:
                return True
    return False

re = if_exist(map, 0)
print(re)

















