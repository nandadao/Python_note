# 练习：将英文语句，根据单词反转。
#      How are you
message = "How are you"
list_temp = message.split(" ")
message = " ".join(list_temp[::-1])
print(message)
