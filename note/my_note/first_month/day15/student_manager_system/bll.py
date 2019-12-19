
# business logic layer 业务逻辑层

class StudentManagerController:
    """
        控制
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
        self.__stu_list.append(stu_target)

    def __generate_id(self, stu_target):
        StudentManagerController.init_id += 1
        stu_target.id = StudentManagerController.init_id

    def remove_student(self, stu_id):
        """
            删除学生
        :param stu_id: int类型，学生编号
        :return: bool 类型，表示是否删除成功
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self, stu_target):
        """
            修改学生信息
        :param stu_target:学生类型，需要修改的信息
        :return:是否修改成功
        """
        for item in self.__stu_list:
            if item.id == stu_target.id:
                item.name = stu_target.name
                item.age = stu_target.age
                item.score = stu_target.score
                return True
        return False

    def order_by_score(self):
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]