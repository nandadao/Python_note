"""
    真值表达式
        如果变量有值，则满足条件。

    条件表达式（三元）
        根据条件，有选择性的为变量进行赋值
    练习:exercise07
"""
# 为false: None  0  0.0  ""
if 5:  # bool(5)
    print("满足条件")

str_input = input("请输入：")
# if str_input != "":
if str_input:  # bool(str_input)
    print("输入了内容")

# if input("请输入性别：") == "男":
#     sex = 1
# else:
#     sex = 0
sex = 1 if input("请输入性别：") == "男" else 0
