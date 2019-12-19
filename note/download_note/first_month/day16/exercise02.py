# 练习1:使用迭代思想，获取元组中所有元素("a","b","c")
tuple01 = ("a", "b", "c")
iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

# 练习2:使用迭代思想，获取字典中所有记录("a":1,"b":2,"c":3)
dict01 = {"a": 1, "b": 2, "c": 3}
iterator = tuple01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key,dict01[key])
    except StopIteration:
        break








