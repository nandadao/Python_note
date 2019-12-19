"""
    继承 - 设计角度
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle, pos):
        print("去", pos)
        vehicle.transport()

class Vehicle:
    def transport(self):
        pass
# ------------------------------------------------
class Car(Vehicle):
    def transport(self):
        print("汽车行驶...")

class Airplane(Vehicle):
    def transport(self):
        print("飞喽...")

lz01 = Person("老张")
c01 = Car()
a01 = Airplane()
lz01.go_to(a01, "东北")
