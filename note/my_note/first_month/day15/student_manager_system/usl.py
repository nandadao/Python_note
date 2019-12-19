
# user show layer 用户显示层


from bll import StudentManagerController
from model import StudentModel


class StudentManagerView:
    """
        视图
    """

    def __init__(self):
        self.__controller = StudentManagerController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)根据成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_students_by_score()


# 这里是为了处理异常的函数
    def __input_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("输入有误，请重新输入")



    def __input_students(self):
        # 循环获取信息
        while True:
            name = input("请输入姓名：")
            if name == "":
                break
            age = self.__input_number("请输入年龄：")

            score = self.__input_number("请输入成绩：")
            stu = StudentModel(name, age, score)
            # 将学生信息交给Controller中的add_student方法
            return self.__controller.add_student(stu)




    # 显示学生__output_students
    def __output_students(self):
        for item in self.__controller.stu_list:
            print(item.id, item.name, item.age, item.score)

    # 删除学生__delete_student
    def __delete_student(self):
        stu_id = self.__input_number("请输入需要删除的学生编号：")
        if self.__controller.remove_student(stu_id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = model.StudentModel()
        stu.id = self.__input_number("请输入编号：")
        stu.name = input("请输入姓名：")
        stu.age = self.__input_number("请输入年龄：")
        stu.score = self.__input_number("请输入成绩：")
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_students_by_score(self):
        self.__controller.order_by_score()
        self.__output_students()