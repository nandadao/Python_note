"""
    bool 运算
    命题：带有判断性质的陈述句
        你是个帅哥。
        真/成立   True
        假/不成立 Flase
    比较运算符  >  <  >= <=  ==  !=
    逻辑运算符 与and   或or   非not
"""
# 比较运算符
print(10 > 15)  # Flase
# str   int
print("10" == 10)  # Flase

# 逻辑运算符

# 一假俱假 --> 必须都是真，结果才是真 --> 并且的关系
print(True and True)# True
print(False and True)# False
print(True and False)# False
print(False and False)# False
# 一真俱真 --> 有一个是真，结果就是真 --> 或者的关系
print(True or True)# True
print(False or  True)# True
print(True or False)# True
print(False or  False)# False
# 取反
print(not True)# False
