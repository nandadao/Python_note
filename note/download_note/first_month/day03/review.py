"""
    复习
    数据的基本运算
        数据
            变量： 名称 = 对象
            类型：None:表示空
                 int：表示整数
                 float：表示小数
                 str：表示文字
                 bool：表示命题真True  伪False

        运算
            转换：  结果 =  类型(待转数据)
                如果待转数据表示没有值，则为false。
            运算符
                算数运算符+ - * ** /  //  %
                增强运算符+= -= *= **= /=  //=  %=
                比较运算符>  <  >= <=  ==  !=
                逻辑运算符and  or  not
                        假   真
                      得满足 一个就行

"""
print(bool(0))#False
print(bool(0.0))#False
print(bool(""))#False
print(bool(None))#False
number01 = 5
result = number01 + 10
# number01 = number01 + 10
number01 += 10
print(number01)# 5

