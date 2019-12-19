"""
    range 整数生成器
    练习：exercise02

    小结：while 根据条件重复执行
         for 遍历可迭代对象
         for + range 根据次数重复执行
"""
for item in range(1, 5, 1):  # 1 2 3 4
    print(item)

for item in range(3):  # 0 1 2
    print(item)

for item in range(20, 25):  # 20 21  22  23  24
    print(item)

for item in range(8, 5, -1):  # 8 7 6
    print(item)
