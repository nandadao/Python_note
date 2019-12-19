"""
    画出下列代码内存图
"""
data01 = 500
# 将变量data01存储的地址 赋值给 变量data02
data02 = data01
# 修改了变量data01存储的地址
data01 = 800
print(data02)  # 500

name01 = "张无忌"
name02 = "赵敏"
name03 = name01 + name02
name04 = "name01+name02"