"""
    练习1：("a", "b", "c")
        使用迭代思想获取，元组中所有元素
    练习2    使用迭代思想获取，字典中所有元素
        {"a":1, "b":2, "c":3}

"""

tuple01 = ("a", "b", "c")
dict01 = {"a":1, "b":2, "c":3}

iterator01 = tuple01.__iter__()
while True:
    try:
        item = iterator01.__next__()
        print(item)
    except StopIteration:
        break


iterator02 = dict01.__iter__()
while True:
    try:
        item = iterator02.__next__()
        print(item, dict01[item])
    except StopIteration:
        break








