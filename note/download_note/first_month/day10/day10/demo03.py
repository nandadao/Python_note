"""
    17:03
"""


class ICBC:
    """
        工商银行
    """
    # 类变量
    total_money = 1000000

    # 类方法
    @classmethod
    def print_total_money(cls):
        # print("总行的钱:",ICBC.total_money)
        print("总行的钱:",cls.total_money)


    def __init__(self,name,money):
        self.name = name
        # 实例变量
        self.money = money
        # 总行的钱减少
        ICBC.total_money -= money

i01 = ICBC("天坛支行",100000)
i02 = ICBC("陶然亭支行",100000)
print(ICBC.total_money)
# print(i01.total_money)
ICBC.print_total_money()


