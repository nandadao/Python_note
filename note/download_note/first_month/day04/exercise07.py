# 练习1:测试你所想的代码。
# 练习2:创建字符串：爱生活，我爱编程。
#    -- 打印第一个字符，打印最后一个字符。
#    -- 打印字符串长度，打印中间的字符
#    -- 打印前三个字符，后三个字符。
#    -- 倒序打印所有字符
message = "爱生活，我爱编程。"
print(message[0])
print(message[-1])
print(len(message))
index = len(message) // 2
print(message[index])
print(message[:3])
print(message[-3:])
print(message[:])  # 从头到尾
print(message[::-1])  # 从尾到头
