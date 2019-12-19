"""
    装饰器
"""
def print_func_name(func):
    def wrapper(*args, **kwargs):  # 合
        print(func.__name__)
        return func(*args, **kwargs)   # 拆
    return wrapper

@print_func_name
def say_hello():
    print("hello")


@print_func_name
def say_goodbye():
    print("goodbye")

say_hello()
say_goodbye()






















