"""
    学生管理系统

    一）
    数据模型类：StudentModel
		数据：编号 id,姓名 name,年龄 age,成绩 score
	逻辑控制类：StudentManagerController
		数据：学生列表 __stu_list
		行为：获取列表 stu_list,添加学生 add_student
"""


class StudentModel:
    """
        模型
    """
    def __init__(self, name="", age=0, score=0.0, id=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    """
        逻辑 
    """
    init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_target):
        """
            添加学生
        :param stu_target: 学生类型对象
        """
        self.__generate_id(stu_target)
        self.stu_list.append(stu_target)

    def __generate_id(self, stu_target):
        StudentManagerController.init_id += 1
        stu_target.id = StudentManagerController.init_id


# -----------------------
# 测试
manager = StudentManagerController()
stu = StudentModel("悟空", 28, 100)
manager.add_student(stu)
for item in manager.stu_list:
    print(item.id, item.name)
