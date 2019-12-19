"""
    练习:在终端中录入商品信息(名称/价格)
        如果名称是空字符，则停止。
        -- 将所有商品名称与价格打印出来(一行一个)
        -- 如果录入了"游戏机",则单独打印其价格.
        -- 要求：重复的商品，不能重复录入。
"""
dict_commodity = {}
while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = float(input("请输入商品价格:"))
    if name not in dict_commodity:
        dict_commodity[name] = price

for key, value in dict_commodity.items():
    print("%s的价格是%.1f" % (key, value))

if "游戏机" in dict_commodity:
    print(dict_commodity["游戏机"])