"""
"""
"""
    练习1：在终端中录人名，要求不能重复，如果空则停止，
        最后打印所有人名（一行一个）
    练习2：
        经理："曹操","刘备","孙权"
        技术："曹操","刘备","张飞","关羽"
                定义数据结构，存储以上信息
                计算是经理也是技术的有谁
                计算是经理不是技术的有谁
                计算不是经理是技术的有谁
                计算身兼一职的是谁
                公司总共有多少人
                张飞是不是经理  True  False
"""
# 练习一
# set_name = set()
# while True:
#     your_name = input("请输入姓名：")
#     if your_name == "":
#         break
#     set_name.add(your_name)
#
# for item in set(set_name):
#     print(item)

# 练习二：
# set_jl = {"曹操","刘备","孙权"}
# set_js = {"曹操","刘备","张飞","关羽"}
#
# print("是经理也是技术的是：",set_jl & set_js)
# print("是经理不是技术的是：",set_jl - set_js)
# print("不是经理是技术的是：",set_js - set_jl)
# print("身兼一职的是谁：",set_js ^ set_jl)
# print("公司总共有多少人：",len(set_js | set_jl))
# print("张飞是经理","张飞" in set_jl)
dict_person = {
    "经理":{"曹操","刘备","孙权"},
    "技术":{"曹操","刘备","张飞","关羽"}
}
print(dict_person["经理"] & dict_person["技术"])
print(dict_person["经理"] - dict_person["技术"])
print(dict_person["技术"] - dict_person["经理"])
print(dict_person["经理"] ^ dict_person["技术"])
print(len(dict_person["经理"] | dict_person["技术"]))

















