


# 老师的
# 装饰器
# def timeis(f):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = f(*args, **kwargs)
#         end_time = time.time()
#         print("%s运行时间%.6f"%(f.__name__, end_time-start_time))
#         return res
#     return wrapper

# def my_decorator(funct):
#     def wrapper():
#         print("装饰器")
#         funct()
#     return wrapper
#
# #使用装饰器
# @my_decorator
# def func1():
#     print("Hello World")
#
#
# func1()

class A(object):
    def start(self):
        self.run()
    def run(self):
        pass

class B(A):
    def run(self):
        print("Ｂ类设计")

b = B()
b.start()















