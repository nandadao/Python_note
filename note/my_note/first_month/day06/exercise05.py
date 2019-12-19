""""""
"""
    练习:在终端中录入多个学生信息(姓名，年龄，成绩，性别) 用字典录入
        如果名称是空字符，则停止。
        -- 将所有学生信息打印出来(一行一个)
        -- 如果录入了"赵敏",则单独打印其信息.
        
        数据结构：
            {
                "张无忌":(25,85,“男”),
                "赵敏“：(24, 100, "女")
                }
"""

dict_information = {}
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = int(input("请输入学生年龄："))
    score = float(input("请输入学生成绩："))
    sex = input("请输入学生性别：")
    dict_information[name] = [age, score, sex]

for key, value in dict_information.items():
    print("%s,年龄%d,成绩%f,性别%s"%(key, value[0], value[1], value[2]))
# print(dict_information)
if "赵敏" in dict_information:
    print("赵敏,年龄%d,成绩%f,性别%s"%
          (
           dict_information["赵敏"][0],
           dict_information["赵敏"][1],
           dict_information["赵敏"][2])
          )








