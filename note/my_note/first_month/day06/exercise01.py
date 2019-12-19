"""
    练习：在终端中录入商品的信息（名称/价格）
        如果名称是空字符，则停止

            1.将所有商品名称与价格打印出来（一行一个）
            2.如果录入了“游戏机”，则单独打印其就价格
            3.要求：重复的商品，不能重复录入
"""

# dict_goods = {}
# while True:
#     goods = input("请输入商品名称：")
#     price = input("请输入商品价格：")
#     if goods == "":
#         if "游戏机" in dict_goods:
#             print(dict_goods["游戏机"])
#         else:
#             for k,v in dict_goods.items():
#                 print("名称：%s,价格：%s"%(k,v))
#             break
#     else:
#         if goods in dict_goods:
#             print("商品重复，请重新输入：")
#             continue
#         else:
#             dict_goods[goods] = price

dict_commodity = {}
while True:
    name = input("请输入名称：")
    if name == "":
        break
    price = float(input("请输入商品价格："))
    if name not in dict_commodity:
        dict_commodity[name] = price

for key, value in dict_commodity.items():
    print("%s的价格是%.f"%(key, value))


if "游戏机" in dict_commodity:
    print(dict_commodity["游戏机"])















