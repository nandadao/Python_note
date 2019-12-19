# 3.（扩展）
# 循环
# 一个小球从100米落下，每次弹回原高度一半，
# 请计算：
# 一：总共弹起多少次（最小弹起的高度0
# .01
# m）
# 二：整个过程，经过多少米

# count = 0
# jump = 0
# height = 100
# while height/2 > 0.01:
#     height /= 2
#     jump += height*2
#     count += 1
# # print(height)
# # print(jump)
# print("总共弹了" + str(count) + "次。")
# print("整个过程，经过了" + str(jump+100) + "米。")
# # print(height)


# 4.
# 判断一个字符串是否为回文：
# 上海自来水来自海上
# （用切片[-len(s) // 2]
# 是否
# 等于 ）

# message = input("请输入一个字符串：")
# # if str_01[:len(str_01) // 2] == str_01[:(-len(str_01) // 2):-1]:
# #     print("是回文")
# # else:
# #     print("不是回文")
#
# if message == message[::-1]:
#     print("是回文")
# else:
#     print("不是回文")

# 5.
# 在终端中，循环录入你喜欢的人。（列表）
# 如果录入空字符串，则打印：
# 一：所有人（一行一个）
# 二：前三个人list01[:3]
# 三：打印总人数len(list01)

list_01 = []
while True:
    favorite = input("请输入你喜欢的人：")
    if favorite:
        list_01.append(favorite)
    else:
        for item in list_01:
            print(item)
        print(list_01[:3])
        print(len(list_01))
        break
