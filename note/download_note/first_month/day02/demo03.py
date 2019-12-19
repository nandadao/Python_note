"""
    数据类型

"""
# 1. None  空对象
# -- 占位
name = None
age = 18
# -- 解除与对象的绑定关系
age = None

# 2. 整数int
# -- 十进制（逢十进一）0 1 2 3 4 .. 9  10
number01 = 10
# -- 二进制（逢二进一）0 1 10
number01 =0b10
# -- 八进制（逢八进一）0 1 .. 7  10
number01 = 0o10
# -- 十六进制（逢十六进一）0 1 ..9  a(10) ..f(15)
number01 = 0x10

# 3. 浮点数 float
number02 = 0.0
print(type(number02))
number02 = 0.0000000000000000000000001
print(number02)# 1e-25

# 4. 字符串 str
name = "qtx"
name = "007"
# 拼接
name = "1.5" + "2.5"
print(name)

# 5. 数据类型转换
# 变量 = 数据类型(数据)
