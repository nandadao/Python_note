

# 生成器 --->  迭代器 + 可迭代对象
# class Generator:
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         ...
#




def my_range(number):
    begin = 0
    while begin < number:
        yield begin   # 暂时离开，再次调用继续执行
        begin += 1


for item in my_range(5):
    print(item)  # 0 1 2 3 4