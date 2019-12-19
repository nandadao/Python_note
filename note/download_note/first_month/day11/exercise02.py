"""
    使用面向对象思想,描述下列情景:
        小明在银行取钱.
"""
class Person:
    def __init__(self, name="",money=0):
        self.name =name
        self.money = money

class Bank:
    def __init__(self,money =0):
        self.money = money

    def draw_money(self,person,value):
        # 银行钱少了
        self.money -= value
        # 人的钱多了
        person.money += value

b01 = Bank(100000)
p01 = Person("小明",0)
b01.draw_money(p01,500)
print("人的钱:",p01.money)
print("银行的钱:",b01.money)





