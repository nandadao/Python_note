"""
    练习1：在终端中录入所有学生的身高，如果录入空，
    则：
        -- 倒序打印所有身高(一行一个)
        -- 打印最高 max()
        -- 打印最低 min()
        -- 打印平均身高 sum() / len()
    要求：思考内存图
"""
list_height = []
while True:
    str_height = input("请输入身高：")
    if str_height == "":
        break
    height = float(str_height)
    list_height.append(height)

for i in range(len(list_height) - 1, -1, -1):
    print(list_height[i])

print(max(list_height))
print(min(list_height))
print(sum(list_height) / len(list_height))
