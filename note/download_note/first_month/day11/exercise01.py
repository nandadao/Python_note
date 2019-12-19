"""
    创建敌人类(姓名,  血量,  攻击力,   防御力)
                  0-1000    0-500   0-100
"""

class Enemy:
    def __init__(self, name, hp, atk=0, defense=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 1000:
            self.__hp = value
        else:
            raise Exception("我不要")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        if 0 <= value <=500:
            self.__atk = value
        else:
            raise Exception("我不要")

    @property
    def defense(self):
        return  self.__defense

    @defense.setter
    def defense(self,value):
        if 0 <= value <= 100:
            self.__defense = value
        else:
            raise Exception("我不要")

e01 = Enemy("悟空", 500, 300, 50)
print(e01.name)
print(e01.hp)
print(e01.atk)
print(e01.defense)
