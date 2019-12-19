"""
    通用操作
    练习:exercise07
"""
# 数学运算符
# +  ×
# 拼接
name01 = "八戒"
name01 += "唐僧"

# 重复
name02 = "唐僧"
name02 *= 2
print(name02)  # 唐僧唐僧

# 比较运算 ==  !=
# 依次比较两个容器中元素,一但不同则返回比较结果。
print("孙悟空" == "唐僧")

# 成员
# 元素 in 容器
# 元素 not in 容器
print("大圣" in "我是齐天大圣")  # True

# 索引：定位单个元素
# 容器名[整数]
message = "我是齐天大圣孙悟空"
print(message[2])
print(message[-2])
# print(message[99999])#IndexError 索引越界

# 切片：定位多个
# 容器名[开始:结束:间隔]
print(message[2:6])
# 开始值不写，默认为开头
print(message[:4])
# 结束值不写，默认为末尾
print(message[::2])  # 我齐大孙空
print(message[2:-3:])  # 齐天大圣
print(message[2:-3:-1])  # 空
print(message[1:100])  # 是齐天大圣孙悟空
