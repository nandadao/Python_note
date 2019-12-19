# 可导出成员
__all__ = ["fun01"]

def fun01():
    print("module02 -- fun01")

class MyClass:
    def fun02(self):
        print("module02 -- fun02")

    @classmethod
    def fun03(self):
        print("module02 -- fun03")

print(__name__)
