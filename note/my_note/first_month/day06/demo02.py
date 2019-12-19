"""
    字典
"""
# 创建
dict01 = {}
dict02 = dict()  # tuple() list()
# 区别：第二个需要放可迭代对象，第一个可以随意放
dict01 = {"悟空": 180, "八戒": 150, "张无忌":170}
# print(dict01)
dict02 = dict([["悟空", 180],["八戒",150]])
# 一定要区分键和值
print(dict02)
# 字典 --> 列表  :只是保留了键
list01 = list(dict01)
print(list01)  # ['悟空', '八戒', '张无忌']

# 添加(key不存在就是添加)
dict01["唐僧"] = 190
print(dict01)
# 修改(key存在就是修改)
dict01["唐僧"] = 180

# 获取如果存在，返回value
# 获取如果不存在，报错
# print(dict01["沙僧"])
# 循环（通过循环获取所有键）
for key in dict01:
    print(key)
# 获取所有value
for value in dict01.values():
    print(value)
# 获取所有key 和  value
for k,v in dict01.items():
    print(k,v)

# 删除
# if "唐僧" in dict01:
del dict01["唐僧"]
del dict01["唐僧"]

print(dict01)












