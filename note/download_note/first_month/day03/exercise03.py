# 练习:获取数字/运算符/数字
#     如果运算符是+ - * /打印结果，否则打印运算符有误.
number_one = float(input("请输入第一个数字："))
operator = input("请输入运算符：")
number_two = float(input("请输入第二个数字："))
if operator == "+":
    print(number_one + number_two)
elif operator == "-":
    print(number_one - number_two)
elif operator == "*":
    print(number_one * number_two)
elif operator == "/":
    print(number_one / number_two)
# 以上条件都不满足
else:
    print("运算符有误")
