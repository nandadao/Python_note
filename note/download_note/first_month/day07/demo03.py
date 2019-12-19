"""
    函数
    练习：exercise07~
"""


# 定义函数  -- 做    改
def attack():
    """
        攻击行为
    """
    print("直拳")
    print("摆拳")
    print("肘击")
    print("瞪")


# 形式参数
def attack_repeat(count):
    """
        重复攻击功能
    :param count:int类型,表示攻击的次数
    """
    for i in range(count):
        print("直拳")
        print("摆拳")
        print("肘击")
        print("瞪")


# 调用函数  -- 用
attack()
attack()
attack()

# 实际参数
attack_repeat(4)
