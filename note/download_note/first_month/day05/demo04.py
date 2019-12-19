"""
    str -->   list
    练习:exercise06
"""
# 需求："0123456789"
# str_result = ""
# for item in range(10):
#     # 每次拼接，产生对象，之前的对象成为垃圾
#     str_result = str_result + str(item)
# print(str_result)

# 频繁修改字符串
list_result = []
for item in range(10):
    # 将字符串存入列表，没有产生垃圾
    list_result.append(str(item))
str_result = "".join(list_result)
print(str_result)

