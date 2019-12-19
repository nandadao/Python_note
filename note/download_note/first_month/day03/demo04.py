"""
    循环语句
    while 条件:
        循环体
    练习：exercise08
"""
while True:
    usd = input("请输入美元：")
    rmb = float(usd) * 7.0336
    print("结果是：" + str(rmb))
    if input("如果输入e退出") == "e":
        break  # 中断

