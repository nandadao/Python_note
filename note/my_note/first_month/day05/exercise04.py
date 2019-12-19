"""
    练习：How are you
        将上面英文语句，按照单词反转
        最后还是字符串
"""

str_01 = "How are you"
list_02 = []
list_01 = str_01.split(" ")

# *****
message = " ".join(list_01[::-1])



print(message)

