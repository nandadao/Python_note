"""
    算数运算
        算数运算符 +  -  * **  / //  %
        增强运算符 +=  -=  *= **=  /=  //=  %=
    练习:exercise04 ~ exercise07
"""
number01 = 5
number02 = 2
# 幂运算： 5 的 2 次方
print(number01 ** number02)
# 除法
print(number01 / number02) # 2.5
print(number01 // number02) # 2
# 余数 -- 获取整数的个位
print(253 % 10)#3

number03 = 10
# 没有改变number03
print(number03 + 5)
print(number03)# 10

# number03 = number03 + 5
# 变量与其他数据进行运算的结果，又赋值给自身.
number03 += 5