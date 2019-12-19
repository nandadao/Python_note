"""
    列表推导式
"""
# 需求：
# list02 = [item for item in list01 if item % 2 != 0]
# print(list02)


"""
    练习
        使用列表推到式生成1--50之间
            能被3或者5整除的数字
        2.使用列表推导式生成5-20之间数字的三次方
"""
list01 = [i  for i in range(1, 51) if i % 3==0 or i % 5 == 0]
print(list01)

list02 = [i**3 for i in range(5, 21) ]
print(list02)



