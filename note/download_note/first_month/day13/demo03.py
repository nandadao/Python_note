"""
    重写
        内置可重写函数
    练习:exercise03
"""
class Car:
    def __init__(self,brand="", price=0.0):
        self.brand = brand
        self.price = price

    # 自定义对象 --> 字符串
    #   对人友好(没限制)
    def __str__(self):
        return "%s汽车的价格是%d"%(self.brand,self.price)

    #   对解释器友好(python语法限制)
    def __repr__(self):
        return 'Car("%s",%d)'%(self.brand,self.price)

c01 = Car("荣威",200000)
print(c01)# <__main__.Car object at 0x7fbff21977f0>
# content = c01.__str__()
# print(content)

c02 = Car("宝马",400000)
# eval ： 将字符串作为python代码执行  -->  灵活
re = eval("1+2*3")
print(re)# 7

# 克隆对象 -- 相同的对象，重新开辟空间再创建一份。  【互不影响】
c03 = eval(c02.__repr__())

c02.brand = "宝宝"
print(c03.brand)






