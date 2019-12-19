"""
    图形管理器
"""

"""
    练习：
        定义图形管理器，记录多个图形
        迭代图形管理器，获取多个图形
        要求:以最快的速度完成嗯
            调试
"""


class PhotoManager:


    """
        可迭代对象
    """
    def __init__(self):
        self.__list_photos = []

    def add_photo(self, skill):
        self.__list_photos.append(skill)

    def __iter__(self):
        for item in self.__list_photos:
            yield item


manager = PhotoManager()
manager.add_photo("圆形")
manager.add_photo("矩形")
manager.add_photo("三角形")


# for item in manager:
#     print(item)


# for循环原理
# 1.获取迭代器
iterator = manager.__iter__()
while True:
    try:
        # 2.获取下一个元素
        item = iterator.__next__()
        print(item)
    # 3.如果没有元素则结束循环
    except StopIteration:
        break





















