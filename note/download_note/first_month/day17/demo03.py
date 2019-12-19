"""
    生成器表达式
    练习:exercise05
"""
list01 = [43, 4, 54, 5, 66, 77]

# 将list01中所有元素增加10之后，存入list02
# list02 = []
# for item in list01:
#     list02.append(item + 10)

list02 = [item + 10 for item in list01]
# for item in list02:
#     print(item)
# -------------------------------------------------
# -------------------------------------------------
# def get_elements():
#     for item in list01:
#         yield item + 10

# generate01 = (item + 10 for item in list01)
# for item in generate01:
#     print(item)

for item in (item + 10 for item in list01 if item % 2):
    print(item)
