"""
    给出字符串，输出每个字符的编码值
"""

# your_str = input("请输入一个字符串")
# for item in your_str:
#     print(item, ord(item))


"""
    循环输入编码值，然后打印出字符
"""
while True:
    your = input("请输入编码值：")
    if your == "":
        break
    else:
        print(chr(int(your)))





