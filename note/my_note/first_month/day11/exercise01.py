"""
    创建敌人类：姓名，血量，攻击力，防御力
        1.限制血量 0-1000
        2.攻击力  0-500
        3.防御力  0-100
"""


class Enemy():
    def __init__(self, name, blood, attack, defense):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.defense = defense

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, value):
        if 0 <= value <= 1000:
            self.__blood = value
        else:
            raise Exception("血量超过范围")

    @property
    def attack(self):
        return self.__a   # 这里的self.__a 跟下面的self.__a相对应的
    @attack.setter
    def attack(self, value):
        if 0 <= value <= 500:
            self.__a = value
        else:
            raise Exception("攻击力超过范围")

    @property
    def defense(self):
        return self.__defense
    @defense.setter
    def defense(self, value):
        if 0 <= value <= 100:
            self.__defense = value
        else:
            raise Exception("防御力超过范围")




e01 = Enemy("悟空", 2, 100, 100)
print(e01.name, e01.blood, e01.attack, e01.defense)









