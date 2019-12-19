"""
    猜拳
       石头  剪刀
       剪刀   布
       布    石头

       随机产生
"""
# import random
# win = ("石头剪刀", "剪刀布", "布石头")
# same = ("石头石头", "剪刀剪刀", "布布")
# choice = ("石头", "剪刀", "布")
# pc1 = choice[random.randint(0, 2)]
# # pc2 = choice[random.randint(0, 2)]
# pc2 = input("请出拳：")
# print(str(pc1)+str(pc2))
# # if str(pc1)+str(pc2) in win or str(pc2)+str(pc1) in win:
# if str(pc2)+str(pc1) in win:
#     print("获胜")
# elif str(pc2)+str(pc1) in same:
#     print("相同重新开始")
# else:
#     print("你输了")



# 统一管理多个数据 ：思想很重要
# import random
# tuple_win = (
#     ("石头", "剪刀"),
#     ("剪刀", "布"),
#     ("布", "石头"),
# )
# tuple_item = ("石头", "剪刀", "布")
#
# item_input  = input("请出拳：")
# # random.randint(0, 2)  # 生成0 1 2
# index_system = random.randint(0, 2)
# item_system = tuple_item[index_system]
#
# if item_input == item_system:
#     print("平局")
# elif (item_input, item_system) in tuple_win:
#     print("你获胜")
# else:
#     print("你失败")


















