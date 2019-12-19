"""
根据面向对象思想，描述下列情景。
   张无忌 教 赵敏九阳神功
   赵敏 教 张无忌玉女心经
   张无忌上班挣了10000元
   赵敏上班挣了8000元

   [核心：数据的不同，使用对象区分。]
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def teach(self, person_other, str_skill):
        print(self.name, "教", person_other.name, str_skill)

    def work(self, money):
        print(self.name, "上班挣了", money)

zwj = Person("张无忌")
zm = Person("赵敏")

zwj.teach(zm, "九阳神功")
zm.teach(zwj, "玉女心经")

zwj.work(10000)
zm.work(8000)
