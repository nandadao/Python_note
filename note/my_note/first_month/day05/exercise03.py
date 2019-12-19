"""
    在终端中循环录入字符串，如果录入空，则打印素有内容
"""
list_input = []
while True:
    str_input = input("请输入字符串：")
    if str_input == "":
        break
    list_input.append(str_input)

print("".join(list_input))

