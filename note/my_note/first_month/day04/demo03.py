"""
    累加1-100之间能被3整除的整数
"""

#
count = 0
for item in range(10, 51):
    unit = item % 10
    if unit == 2 or unit == 5 or unit == 9:
        continue
    else:
        count += item
print(count)
