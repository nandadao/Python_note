class Vector1:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        return Vector1(self.x + other.x)



v01 = Vector1(10)
print(type(v01))