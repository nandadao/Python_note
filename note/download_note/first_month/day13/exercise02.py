"""
    创建父类
        车(品牌、价格)
    创建子类
        电动车(电池容量、充电速度)
    画出内存图
"""


class Car:
    def __init__(self, brand="", price=0.0):
        self.brand = brand
        self.price = price


class Electrocar(Car):
    def __init__(self, brand="", price=0.0, battery_capacity=0, charging_speed=0):
        super().__init__(brand,price)
        self.battery_capacity = battery_capacity
        self.charging_speed = charging_speed


e01 = Electrocar("荣威", 200000, 100000, 60)
print(e01.brand)
print(e01.price)
print(e01.battery_capacity)
print(e01.charging_speed)
