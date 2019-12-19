
"""
    主动抛异常  --> 快速传递错误信息
    自定义异常类 --> 封装数据
"""

class AgeError(Exception):
    def __init__(self, message="", code="", id=0):
        self.message = message
        self.code = code
        self.id = id


class Wife:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.age
    @age.setter
    def age(self, value):
        if 22<= value <=65:
            self.__age = value
        else:
            #第一步
            # raise AgeError("年龄超过范围了", "if 22<= value <=65:", 1001)
            raise Exception("年龄超过范围了", "if 22<= value <=65:", 1001)
# 第二步
try:
    w01 = Wife(10)

# 给异常对象起一个别名
# except  AgeError as  e:
#     print("处理逻辑")
#     print(e.code)
#     print(e.message)
#     print(e.id)
except Exception as e:
    print("处理逻辑")
    print(e.args[0])
    print(e.args[1])
    print(e.args[2])

