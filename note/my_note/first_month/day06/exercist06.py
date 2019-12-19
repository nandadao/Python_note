
"""
    练习:在终端中录入多个学生信息(姓名，年龄，成绩，性别) 用字典录入
        如果名称是空字符，则停止。
        -- 将所有学生信息打印出来(一行一个)
        -- 打印最后一个学生信息

        数据结构：
            [
                {"name":"张无忌","age":25,"score":85,"sex":“男”},
                {"赵敏“,24, 100, "女"},
                ]
                
                
            总结：使用字典与列表的适用性
                 字典的优缺点:
                            
                 列表的优缺点:
                            优点：
                                有序性，可以按照序号找信息
                            缺点：
                                预留空间，浪费内存
"""

list_information = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = int(input("请输入学生年龄："))
    score = float(input("请输入学生成绩："))
    sex = input("请输入学生性别：")
    list_information.append({"name":name,"age":age, "score":score, "sex":sex})

for item in list_information:
    print("%s,年龄%d,成绩%f,性别%s"%(item["name"], item["age"], item["score"], item["sex"]))
item = list_information[-1]
print("姓名%s,年龄%d,成绩%f,性别%s" % (item["name"], item["age"], item["score"], item["sex"]))

