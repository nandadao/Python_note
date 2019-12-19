"""
    学生管理系统

    一）
    数据模型类：StudentModel
		数据：编号 id,姓名 name,年龄 age,成绩 score
	逻辑控制类：StudentManagerController
		数据：学生列表 __stu_list
		行为：获取列表 stu_list,添加学生 add_student
		2.删除
		3.修改，学生update_student(stu_info)
		4.排序根据成绩排序(升序)
		    order_by_score()
	    5.录入学生信息
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


    def remove_student(self, stu_id):
        # for item in self.__stu_list:
        #     if item.id == id:
        #         del item
        #         return True
        #     else:
        #         return False
        # 老师的答案
        """
            删除学生
        :param stu_id:int类型，学生编号
        :return: bool 类型，表示是否删除成功
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False

    # 修改学生信息(画内存图)
    def update_student(self, stu_target):
        for item in self.__stu_list:
            if item.id == stu_target.id:
                item.name = stu_target.name
                item.age = stu_target.age
                item.score = stu_target.score
                return True
        return False

    # 4.根据成绩升序排序
    def order_by_score(self):
        for r in range(len(self.__stu_list)-1):
            for c in range(r+1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c],self.__stu_list[r]

class StudentManagerView:
    """
        视图
    """
    def __init__(self):
        self.__controller = StudentManagerController()  # 一个界面对应一个控制

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)根据成绩升序显示学生")

    def __select_menu(self, ):
        item = input("请输入选项：")
        if item == "1":  # 提示，输入姓名，年龄。。。
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__order_by_score()


    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        # 只是调用逻辑里的方法，判断是否传入对象
        # 循环获取信息
        # 将学生信息交给Controller中的add_student方法
        while True:
            name = input("请输入姓名")
            if name == "":
                break
            age = int(input("请输入年龄"))
            score = int(input("请输入成绩"))
            stu = StudentModel(name, age, score)
            self.__controller.add_student(stu)

    def __output_students(self):  # 显示学生信息
        for item in self.__controller.stu_list:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):  # 删除学生

        stu_id = int(input("请输入要删除学生的id:"))
        if self.__controller.remove_student(stu_id):
            print("删除成功")
        else:
            print("删除失败")


    def __modify_student(self):  # 修改学生信息
        # # while True:
        # id = input("请输入要修改学生的id:")
        # # if id == "":
        # #     break
        # for item in self.__controller.stu_list:
        #     if item.id  == int(id):
        #         name = input("请输入姓名：")
        #         age = int(input("请输入年龄："))
        #         score = int(input("请输入分数："))
        #
        #         stu = StudentModel(name, age, score, int(id))
        #         self.__controller.update_student(stu)
        #     else:
        #         print("输入有误")
        stu = StudentModel()
        stu.id = int(input("编号："))
        stu.name = input("名字")
        stu.age = int(input("年龄"))
        stu.score = int(input("成绩"))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")



    def __order_by_score(self):
        self.__controller.order_by_score()
        self.__output_students()



view = StudentManagerView()
view.main()















# -----------------------
# 测试
manager = StudentManagerController()
stu = StudentModel("悟空", 28, 100)
manager.add_student(stu)


manager.add_student(StudentModel("唐僧", 25, 95))
re = manager.remove_student(1002)
print(re)  # True

re = manager.remove_student(1005)
print(re)


# 修改学生def update_student(stu_info)
re = manager.update_student(StudentModel("孙悟空", 29, 99, 1001))
print(re)  # True
re = manager.update_student(StudentModel("孙悟空", 29, 99, 1006))
print(re)  # False

# 排序
manager.add_student(StudentModel("唐僧1", 25, 75))
manager.add_student(StudentModel("唐僧2", 25, 55))
manager.add_student(StudentModel("唐僧3", 25, 10))
manager.add_student(StudentModel("唐僧4", 25, 25))

manager.order_by_score()





for item in manager.stu_list:
    print(item.id, item.name, item.score)
