"""
    面向对象：描述
        小明在银行取钱，

"""

# 我的思路
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#
#     def get_money(self, bank, money):
#         print("取出钱数为：", money)
#         bank.reduce_money(money)
#
# class Bank:
#     def reduce_money(self, money):
#         print("银行少了钱数为：", money)

# 老师的思路
class Person:
    def __init__(self, name="", money=0):
        self.name = name
        self.money = money

class Bank:
    def __init__(self, money=0):
        self.money = money

    def draw_money(self,person, value):
        # 银行的钱少了
        self.money -= value
        # 人的钱多了
        person.money += value

b01 = Bank(10000)
p01 = Person("小明", 0)
b01.draw_money(p01, 500)
print(b01.money)
print(p01.money)
























