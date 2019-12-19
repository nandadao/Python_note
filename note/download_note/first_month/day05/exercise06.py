# 练习:在终端中循环录入字符串，如果录入空，则打印所有内容。

list_result = []
while True:
    str_input = input("请输入内容：")
    if str_input == "":
        break
    list_result.append(str_input)

str_result = "".join(list_result)
print(str_result)
