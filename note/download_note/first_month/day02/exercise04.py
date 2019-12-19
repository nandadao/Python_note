"""
    练习：收银台
    在终端中录入一个商品单价  5
    再录入一个购买数量 3
    最后录入支付金额 20
    计算应该找回多少钱 5
"""
# 1. 获取数据
str_price = input("请输入商品单价：")
float_price = float(str_price)
str_count = input("请输入数量：")
int_count = int(str_count)
money = float(input("请输入金额："))
# 2. 逻辑计算
result = money - float_price * int_count
# 3. 显示结果
print("应该找回:" + str(result))
