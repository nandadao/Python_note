""""
    练习1：在终端中录入所有学生的身高，如果录入空：
        倒序打印所有身高一行一个
        打印最高max
        打印最低min
        打印平均sum / len()
    要求：思考内存图
"""
# list_height = []
# while True:
#     height = input("请输入学生身高：")
#     if height == "":
#         break
#     else:
#         list_height.append(float(height))
# #
# for item in range((len(list_height)-1):-1:-1):
#     print(list_height[item])
# print(list_height[::-1])
# print(max(list_height))
# print(min(list_height))
# print(sum(list_height)/len(list_height))

# 在列表中找出最大元素（不使用max)

# 找最大算法
list01 = [10, 3, 1, 9, 99, 111, 222]
the_max = list01[0]
# for i in list01:
#     if i >= the_max:
#         the_max = i
# print(the_max)

for i in range(1, len(list01)):
    if list01[i] > the_max:
        the_max = list01[i]

print(the_max)
