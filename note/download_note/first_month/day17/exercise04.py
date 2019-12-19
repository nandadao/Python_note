"""
    练习：定义my_zip函数，实现下列效果。
    for item in my_zip(list02, list03):
        print(item)
"""


def my_zip(iterable01, iterable02):
    for i in range(len(iterable01)):
        yield (iterable01[i], iterable02[i])


list02 = ["悟空", "八戒", "唐僧"]
list03 = [101, 102, 103]
for item in my_zip(list02, list03):
    print(item)

for item in zip(list02, list03):
    print(item)
