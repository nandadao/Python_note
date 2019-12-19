# 做一个全局变量：

"""
    2048 游戏核心算法

    1.算法
    2.(架构)设计


    1.算法方面的优点：
        1.将维思想：把二维变成一维（因为行与行，列与列，相对独立，
                   所以可以将二维列表的操作，转换为一维列表操作）
                 对矩阵进行转置，然后可以对列操作转化为行
        2.高内聚
            就是说，每个函数的内部小而精。
             核心流程：列  -->  行  --> 去除零  --> 合并(相邻相同)i = i + (i+1)


"""

# 1.定义函数，将零元素移动到末尾，
# 输入[2, 0, 4, 0]
# 输出[2 ,2, 0, 0]
# 这一步，不需用有返回值，因为list_merge已经改变了
# def move_0_to_last(list_input):
#     for i in range(len(list_input)):
#         if list_input[i] == 0:
#             list_input.append(0)
#             list_input.pop(i)

list_merge = [0, 2, 2, 0]  # 变成2 ,2, 0, 0
def zero_to_end():
    for i in range(len(list_merge)-1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

zero_to_end()
# 老师的答案
# 核心思想，倒序删除0元素，后面追加0元素



# move_0_to_last(lsit_merge)
# print(lsit_merge)


# 2.定义函数，合并相同元素(非零)
# 输入[2 ,2, 0, 0]
# 输出[4, 0, 0, 0]
# 输入[2 ,0, 0, 2]  --> 调用一下第一个函数，
# 输出[4, 0, 0, 0]
# 不用返回值
# 输出[2 ,0, 2, 2] --> [2, 2, 2, 0]
# 输入[4, 2, 0, 0]
# 输出[8 ,8,8, 8]
# 输入[16, 16, 0, 0]
# 即相邻的元素相加
# list01 = [8, 8, 8, 8]
# def sum_same_number(list_input):
#     zero_to_end(list_input)
#     for i in range(len(list_input)-1):
#         if list_input[i] == list_input[i + 1]:
#             list_input[i] = list_input[i] + list_input[i + 1]
#             list_input[i + 1] = 0
#             zero_to_end(list_input)


# 老师
def merge():
    # 核心思想：先将0与元素移动到末尾，再判断相邻相同
    zero_to_end()
    for i in range(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)



# sum_same_number(list01)
# print(list01)




map = [
    [2, 0, 2, 0],
    [2, 4, 2, 0],
    [0, 2, 2, 0],
    [2, 0, 4, 2],
]
# 3.定义函数，向左移动
# 提示：每一行交给list_merge,再调用练习2
# 借助第二个函数

# def move_to_left(list_input):
#     for i in list_input:
#         sum_same_number(i)


# 老师
def move_left():
    global list_merge
    for line in map:
        list_merge = line   # 将二维列表中的每一行，交给全局变量
        merge()


# move_left()
# print(map)




# move_to_left(map)
# for i in map:
#     print(i,end="\n")
# # print(map)



# 4.定义函数，向右移动
# 提示：将每行反向切片交给list_merge，再调用练习2

# def move_to_right(list_input):
#     for i in range(len(list_input)):
#         sum_same_number(list_input[i])
#         list_input[i] = list_input[i][::-1]


# 老师
def move_right():
    global list_merge
    for line in map:
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge







# 画内存图，才能理解


# move_right()
# print(map)




# move_to_right(map)
# for i in map:
#     print(i,end="\n")
# # print(map)

# map = [
#     [2, 0, 2, 0],
#     [2, 4, 2, 0],
#     [0, 2, 2, 0],
#     [2, 0, 4, 2],
# ]

# [1][0]  -- [0][1]
# [2][0] --- [0][2]
# [2][1]  - - [1][2]


# 5.定义函数，向上移动
# 提示：方阵转置，再调用练习3,（左移）

# 方阵转置
def list_to_list(list_input):
    for c in range(1, len(list_input)):
        for r in range(c, len(list_input)):
            list_input[r][c - 1], list_input[c - 1][r] = list_input[c - 1][r], list_input[r][c - 1]
# 向上移动
# def move_to_up(list_input):
#     list_to_list(list_input)
#     move_to_left(list_input)
#     list_to_list(list_input)

# 老师
def move_up():
    list_to_list(map)
    move_left()
    list_to_list(map)

# move_up()
# print(map)


# move_to_up(map)
# for i in map:
#     print(i,end="\n")



# 6.定义函数，向下移动
# 提示：方阵转置，再调用练习4

# def move_to_down(list_input):
#     list_to_list(list_input)
#     move_to_right(list_input)
    # list_to_list(list_input)
#
# move_to_down(map)
# for i in map:
#     print(i,end="\n")


def move_down():
    list_to_list(map)
    move_right()
    list_to_list(map)

move_down()
for i in map:
    print(i, end="\n")
# print(map)
















