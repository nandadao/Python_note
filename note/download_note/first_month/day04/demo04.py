"""
    字符串
    练习:exercise05
"""
# 1. 不可变：创建新字符串对象，替换变量地址。
#        没有改变原有字符串
name = "悟空"
# id 函数可以返回对象真实内存地址
print(id(name))
name = "齐天大圣"
print(id(name))
print(name)

# 2. 编码
# 字 -->  数
print(ord("a"))   # 97
print(ord("A"))   # 65
# 数 -->   字
print(chr(97))   # 97
