# 练习:将下列代码，定义到函数中.
def each_unit_sum(str_number):
    sum_value = 0
    for item in str_number:
        sum_value += int(item)
    return sum_value


re = each_unit_sum("1231234234")
print(re)
