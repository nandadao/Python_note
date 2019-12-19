"""
    学生管理系统

    一）
    数据模型类：StudentModel
		数据：编号 id,姓名 name,年龄 age,成绩 score
	逻辑控制类：StudentManagerController
		数据：学生列表 __stu_list
		行为：获取列表 stu_list,添加学生 add_student，
"""
class StudentModel:
    pass


class StudentManagerController:
    pass

#-----------------------
# 测试
manager = StudentManagerController()

stu = StudentModel("悟空",28,100)

manager.add_student(stu)

for item in manager.stu_list:
    print(item.id,item.name)


