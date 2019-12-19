"""
    通用操作

"""
# name = "八戒"
# print(id(name))
# name += "唐僧"
# print(id(name))
# print(name)
#
# name02 = "唐僧"
# name02 *= 2
# print(name02)

# 比较：依次比较两个容器中元素大小，一旦不同则返回比较结果
# print("孙悟空" > "唐僧")
# print(ord("孙"), ord("唐"))
#
#
# # 成员比较
# print("大圣" in "我是齐天大圣")


# 索引
# 0 1  2  3  。。。  len(s)-1
# -len(s)            -2  -1
# 容器名[索引]
message = "我是齐天大圣孙悟空"
# print(message[3])
# print(message[333])  # 索引越界

# 切片
# 容器名[开始：结束：间隔]
print(message[2:6])
print(message[:4])  # 开始值不写，默认为开头
print(message[::2]) # 结束值不写默认为末尾
print(message[2:-3:1])
print(message[2:-3:-1]) # 空的，什么都没有
print(message[-100:100])




















