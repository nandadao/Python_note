"""
 创建技能类（数据：技能名称,冷却时间,消耗法力,攻击比例）
                          0-60    0-100   0 - 1
"""


class Skill:
    def __init__(self, name="", cd=0, cost_SP=0, atk_ratio=0):
        self.name = name
        self.cd = cd
        self.cost_SP = cost_SP
        self.atk_ratio = atk_ratio

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        if 0 <= value <= 60:
            self.__cd = value
        else:
            raise Exception("我不要")

    @property
    def cost_SP(self):
        return self.__cost_SP

    @cost_SP.setter
    def cost_SP(self, value):
        if 0 <= value <= 100:
            self.__cost_SP = value
        else:
            raise Exception("我不要")

    @property
    def atk_ratio(self):
        return self.__atk_ratio

    @atk_ratio.setter
    def atk_ratio(self, value):
        if 0 <= value <= 1:
            self.__atk_ratio = value
        else:
            raise Exception("我不要")

s01 = Skill("降龙十八掌", 60, 100, 1)
print(s01.name)
print(s01.cd)
print(s01.cost_SP)
print(s01.atk_ratio)
