"""
    猜拳
        胜利策略：
            石头  剪刀
            剪刀  布
            布   石头
            10:18
"""
import random

# 胜利策略
tuple_win = (
    ("石头", "剪刀"),
    ("剪刀", "布"),
    ("布", "石头")
)
# 选项
tuple_item = ("石头", "剪刀", "布")
# 玩家输入的选项
item_input = input("请输入：")
# 机器输入
index_system = random.randint(0, 2)  # 0  1   2
item_system = tuple_item[index_system]  # 石头 剪刀 布
if item_input == item_system:
    print("平局")
elif (item_input, item_system) in tuple_win:
    print("胜利")
else:
    print("失败")
