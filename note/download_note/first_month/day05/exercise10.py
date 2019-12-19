# 画出下列代码内存图：
list01 = [10, (20, 30), 40]
list02 = list01[:]
list01[1] = "悟空"
print(list02)
# -------------
name01 = "唐僧"
names = ["悟空", "八戒"]
tuple01 = (name01, names, "白龙马")
name01 = "唐三藏"
names[0] = "孙悟空"
print(tuple01)