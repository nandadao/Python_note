"""
    钱够 --> 应找回
    否则 --> 钱不够
"""
str_price = input("请输入商品单价：")
float_price = float(str_price)
str_count = input("请输入数量：")
int_count = int(str_count)
money = float(input("请输入金额："))
# 2. 逻辑计算
result = money - float_price * int_count
# 3. 显示结果
if result >= 0:
    print("应该找回:" + str(result))
else:
    print("钱不够")
# 11:27

