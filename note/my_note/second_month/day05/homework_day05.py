"""
	质数又被称为素数，是指一个大于1的自然数，
	除了1和它自身外，不能被其它自然数整除，
	且其个数是无穷的，具有许多独特的性质，现如今多被用于密码学上。
	
	求100000以内的质数之和
"""
# 自己的想法
# 做一个生成器，需要一个加一个

import time

# def prime():
# 	# 求质数
#
# 	for item in range(2, 1000):  # 5
# 		if item == 2:
# 			yield item
# 		for i in range(2, item):  # (2, 5)
# 			if item % i == 0:
# 				break
#
# 		yield item
#
start = time.time()
def prime():
	for i in range(2,100000):
		for j in range(2, i):
			if (i % j) == 0:
				break
		else:
			# num.append(i)
			yield i
	# print(num)






# prime()
# for i in prime():
# 	print(i)
#


i = 0
for item in prime():
	i += item
stop = time.time()
use_time = stop - start
print("使用迭代器方法耗时：", use_time)
print("100000以内质数的和是：", i)


# 使用迭代器方法耗时： 0.32865428924560547
# 10000以内质数的和是： 5736396
		





















