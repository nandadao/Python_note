"""
    定义图形管理器：
        1.存储所有图形
        2.计算所有图形的总面积
    圆形：
        pi * r **2
    矩形:
        l * w
    需求变化：
        还可能增加新图形
    要求：
        图形管理器满足开闭原理
"""


# 老师答案
class GraphicManager:
    def __init__(self):
        self.__list_graphics = []

    def add_graphics(self, graphic):
        self.__list_graphics.append(graphic)

    def get_total_area(self):
        sum_area = 0
        for item in self.__list_graphics:
            sum_area += item.calculate_area()
        return sum_area


class Graphic:
    def calculate_area(self):
        """
            计算面积的逻辑
        :return: float
        """
        pass


# -----------------------上面的是架构师做的
class Circle(Graphic):
    def __init__(self, r=0):
        self.radius = r

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectanlge(Graphic):
    def __init__(self, l=0, w=0):
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w



# 我写的答案
# class PictureManager:
#
#     list_picture = []
#     area_picture = 0
#
#     def memory(self, target):
#         PictureManager.list_picture.append(target)
#
#
#     def area(self, target):
#         PictureManager.area_picture += target.count()
#
#
# class Obj:
#     pass
#
# # ------------------------
# class
