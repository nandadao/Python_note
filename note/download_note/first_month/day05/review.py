"""
    复习
        容器
            通用操作：+  ×  == !=  in  索引  切片
            字符串str：存储字符编码，不可变，序列
            列表：存储变量，可变，序列
"""
# 创建
list01 = [1, 2, 34, 45, 56, 6]
list02 = list("我爱编程")

# 添加
list01.append("end")
list01.insert(2, "ok")

# 修改
# --索引
list01[0] = "a"
# --切片
# 遍历右边数据，依次赋值给左边
# list01[1:4] = "bcd"
# list01[1:4] = []
# list01[1:4] = [100]
# list01[1:4] = [324,345,55,4667,75]
# list01[1:1] = [324,345,55,4667,75]
list01[10:10] = [324, 345]
# --循环
# for item in list01:
#     item = None
# for i in range(len(list01)):
#     list01[i] = None

# 删除
if "no" in list01:
    list01.remove("no")
del list01[0]
del list01[1:3]

# 获取
# --索引
a = list01[0]
# --切片
print(id(list01))
# 通过切片获取元素，会创建新列表。
result = list01[:3]
print(id(result))
# --循环
for item in list01:
    print(item)
# 需求：倒序获取所有元素
# 不建议
# for item in list01[::-1]:
#     print(item)
for i in range(len(list01) - 1, -1, -1):
    print(list01[i])
