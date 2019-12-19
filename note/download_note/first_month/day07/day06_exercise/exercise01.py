
list01 = [
    10,{101:"悟空"}
]
list02 = list01[:]
# 修改的是字典的值
list01[1][101] = "孙悟空"
print(list02)

dict01 = {
    "唐僧":[25,"男"],
    "八戒":[28,"男"],
}
dict02 = dict01
dict01["八戒"][0] = 29
print(dict02)
