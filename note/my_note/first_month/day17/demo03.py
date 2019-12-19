"""
    生成器表达式
"""
list01 = [11, 32, 3, 2 ]
# 将list01 中所有元素增加10之后，存入list02

list02 = []
def get_elements():
    for item in list01:
        yield item + 10

generate01 = (item + 10 for item in list01)
print(type(generate01))






















