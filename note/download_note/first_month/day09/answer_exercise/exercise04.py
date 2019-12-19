"""
    质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
    定义函数，获取指定范围内的所有质数。
    输入：2,20
    输出：[2, 3, 5, 7, 11, 13, 17, 19]
"""

def is_prime(number):
    for item in range(2, number):
        if number % item == 0:
            return False
    return True


def get_prime(begin, end):
    # list_result = []
    # for num in range(begin, end):
    #     if is_prime(num):
    #         list_result.append(num)
    # return list_result
    return [num for num in range(begin, end) if is_prime(num)]

print(get_prime(2,20))