"""
    迭代器 --> yield --> 生成器
    练习:exercise02~04
"""

""" 伪代码
class Generator: 
    # 生成器 --> 迭代器 +  可迭代对象
    def __iter__(self):
        return self
    
    def __next__(self):
        ... 
"""

def my_range(stop):
    begin = 0
    while begin < stop:
        yield begin# 暂时离开，再次调用继续执行
        begin += 1

for item in my_range(99999999999):
    print(item)  # 0 1 2 3 4

# mr = my_range(99999999999)
# iterator = mr.__iter__()
# while True:
#     try:
#         # 2. 获取下一个元素
#         item = iterator.__next__()
#         print(item)
#     # 3. 如果没有元素则结束循环
#     except StopIteration:
#         break



