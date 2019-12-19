"""
    多继承
        继承：隔离变化
        多继承：被多个变化所隔离，不是代码的复用。
        17:06
"""
class A:
    def fun01(self):
        print("A -- fun01")

class B(A):
    def fun01(self):
        print("B -- fun01")


class C(A):
    def fun01(self):
        print("C -- fun01")

class D(C,B):
    def fun01(self):
        print("D -- fun01")
        # 如果父级别有多个重名方法，使用的是继承列表最左边的。
        #　如果想调用其他类，则使用类名访问。
        # super().fun01()# ?
        B.fun01(self)

d01 = D()
d01.fun01()

# 同名方法解析顺序
print(D.mro())

