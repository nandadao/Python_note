


class Class01:
    def __sub__(self, other):
        return Class01(self.x - other.x)

    def __str__(self):
        return str(self.x)

    def __init__(self, x=0):
        self.x = x

    def __truediv__(self, other):
        return Class01(self.x // other.x)

c01 = Class01(20)
c02 = Class01(10)
print(c01 - c02)

print(c01 // c02)











