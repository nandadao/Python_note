"""
    列表推导式嵌套
    练习:exercise06
    15:25
"""
# 列表全排列
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["雪碧", "可乐", "牛奶", "咖啡"]
# list03 = []
# for r in list01:
#     for c in list02:
#         list03.append(r + c)
list03 = [r + c for r in list01 for c in list02]
print(list03)
