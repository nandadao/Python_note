import random
tuple_win =  (
    ("石头", "剪刀"),
    ("剪刀", "布"),
    ("布", "石头"),
)
tuple_item  = ("石头", "剪刀", "布")

itme_input = input("请出拳：")
index_system = random.randint(0,2)
item_system = tuple_item[index_system]

if itme_input == item_system:
    print("平局")
elif (itme_input, item_system) in tuple_win:
    print("获胜")
else:
    print("失败")
















