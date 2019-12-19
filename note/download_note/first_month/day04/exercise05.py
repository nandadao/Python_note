"""
    练习1:在终端中录入一个字符串，打印每个字符的编码。
    练习2:在终端中重复录入编码值，然后打印字符串。
          如果录入的编码值是空字符串，则退出。
"""
# 1.
# str_input = input("请输入内容：")
# for item in str_input:
#     print(ord(item))

# 2.
while True:
    str_input = input("请输入编码值：")
    if str_input == "":
        break
    char = chr(int(str_input))
    print(char)




