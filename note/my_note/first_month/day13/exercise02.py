class Car:
    def __init__(self, paizi="", price=0):
        self.paizi = paizi
        self.price = price


class Diandong(Car):
    def __init__(self, paizi="", price=0,dianci=0, speed=0):
        super().__init__(paizi, price)
        self.dianci = dianci
        self.speed = speed


d01 = Diandong("jfj", 1000, 300, 120)
print(d01.price)
print(d01.dianci)
print(d01.paizi)
print(d01.speed)

