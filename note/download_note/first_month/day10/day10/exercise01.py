"""
    练习:创建狗类
            数据:爱称,品种,价格
            行为:叫
        创建2个狗对象,分别调用叫的行为
        画出内存图
"""

# 11:30
class Dog:
    def __init__(self, pet_name = "", breed = "", price=3000):
        self.pet_name = pet_name
        self.breed = breed
        self.price = price

    def shout(self):
        print(self.pet_name, "旺旺叫")

# 2对象 2套数据
d01 = Dog("米咻","拉不拉多")
d02 = Dog("黑米","拉不拉多",3500)
# 1个方法被多个对象共享
d01.shout()
d02.shout()


















