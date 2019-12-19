"""
    练习：创建狗类，
            数据：爱称，品种，价格
            行为：叫

        要求：1.创建2个狗对象，分别调用叫的行为，
             2.画出内存图，
"""

class Dog:
    """
        创建一个狗类
    """
    def __init__(self,call, breed, price):
        """
            创建一个数据
        """
        self.call = call
        self.breed = breed
        self.price = price

    def bite(self):
        print(self.call,"要咬人")
#
#
# # 多了一个对象，相当于多了一套数据
# dog01 = Dog("旺财","金毛", 3000)
# dog02 = Dog("大黄", "中华田园犬", "无价")
#
#
# # 1个方法被多个对象共享
# dog01.bite()
# dog02.bite()


"""
    练习2
"""
d01 = Dog("旺财","金毛", 3000)
d02 = d01
d01.call = "小黄"
print(d02.call)

















