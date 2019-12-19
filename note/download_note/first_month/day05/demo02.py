"""
    深浅拷贝
"""
import copy

list01 = [10,[20,30]]
# list02 = list01[:]
# 浅拷贝 == 切片
list02 = list01.copy()
# 深拷贝
list03 = copy.deepcopy(list01)
# 优点：互不影响
list01[1][0] = 200
# 缺点：占用内存过多
print(list03)