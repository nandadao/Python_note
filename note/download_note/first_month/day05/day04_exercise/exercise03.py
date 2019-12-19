"""
在终端中，循环录入你喜欢的人，如果空字符串，
   则打印：
   -- 所有人（一行一个）
   -- 前三个人
   -- 总人数
""" 
list_name = []
while True:
    name = input("请输入人名：")
    if name == "":
        break
    list_name.append(name)

for item in list_name:
    print(item)

print(list_name[:3])

print(len(list_name))