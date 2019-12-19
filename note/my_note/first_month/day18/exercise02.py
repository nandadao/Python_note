"""
    闭包应用
"""

# 逻辑连续：得到了1000元，然后继续购买商品
def give_gife_money(money):
    def child_by(target, price):

        nonlocal money
        if money > price:
            print("孩子买了", target, "花了", price)
            money -= price
        else:
            print("没钱了")

    return child_by

action = give_gife_money(1000)
action("变形金刚", 499)
action("芭比娃娃", 300)
action("挖掘机", 500)




















