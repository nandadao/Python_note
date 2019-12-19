# 练习:在终端中录入一个数字，作为边长，打印矩形。
#  输入：4         6
# ****           ******
# *  *           *    *
# *  *           *    *
# ****           *    *
#                *    *
#                ******
# 16:50
number = int(input("请输入数字："))
print("*" * number)

for item in range(number - 2):
    print("*" + " " * (number - 2) + "*")

print("*" * number)
