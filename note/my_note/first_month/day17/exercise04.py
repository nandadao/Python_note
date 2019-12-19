"""
    练习：定义函数：my_enumerate函数，实现下列效果
"""

list01 = [1, 2, 55, 3]
dict01 = {"a":1, "b":2, "c":3}

def my_enumerate(iterable):
    my_index = 0
    for item in iterable:
        yield (my_index,item)
        my_index += 1


# for index, item in my_enumerate(list01):
#     print(index, item)
# print("-----------------")
# for index, item in my_enumerate(dict01):
#     print(index, item)
#
# print("————————————————————")
# for index, item in enumerate(dict01):
#     print(index, item)


list02 = ["悟空", "八戒", "唐僧"]
list03 = [101, 102, 103]

# 练习2：自定义一个函数my_zip, 实现下列效果
def my_zip(iterable01, iterable02):
    for i in range(len(iterable01)):
        yield (iterable01[i], iterable02[i])


for item in my_zip(list02,list03):
    print(item)
# ('悟空', 101)
# ('八戒', 102)
# ('唐僧', 103)







