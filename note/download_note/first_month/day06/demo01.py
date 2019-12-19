"""
    字典 dict
"""
# 创建
dict01 = {}
dict02 = dict()

dict01 = {"悟空": 180, "八戒": 150, "张无忌": 170}
# 其他可迭代对象(格式)  -->  字典
dict02 = dict([("悟空", 180), ("八戒", 150)])

# 字典 --> 列表（键）
list01 = list(dict01)
print(list01)

# 添加（key不存在）
dict01["唐僧"] = 190
# 修改（key存在）
dict01["唐僧"] = 180

# 获取
# -- 通过key
#     如果存在，返回value。
print(dict01["悟空"])
#      如果不存在，报错。
if "沙僧" in dict01:
    print(dict01["沙僧"])

# -- 通过循环
#    获取所有key
for key in dict01:
    print(key)
#    获取所有value
for value in dict01.values():
    print(value)
#   获取所有key--value
# for kv in dict01.items():# 遍历结果是元组
#     print(kv)
for key,value in dict01.items():
    print(key)
    print(value)
# 删除
if "唐僧" in dict01:
    del dict01["唐僧"]
    print(dict01)
