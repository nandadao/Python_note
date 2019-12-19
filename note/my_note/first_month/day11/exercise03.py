"""
    面向对象：
        防守者攻击敌人，敌人受伤，还可能死亡
"""

# class Defenser:
#     def __init__(self, name="", attack_blood=0):
#         self.name = name
#         self.attack_blood = attack_blood
#
# class Enemy:
#     def __init__(self, blood):
#         self.blood = blood
#
#     def attacked(self, enemy, value):
#
#         self.blood -= value
#
#
# d01 = Defenser("大炮", 100)
# e01 = Enemy(1000)



# 实例成员找对象
class Defender:
    def __init__(self, atk=0):
        self.atk = atk
    def attack(self, target):
        print("走你")
        target.damage(self.atk)


class Enemy:
    def __init__(self, hp=0):
        self.hp = hp
    def damage(self, value):
        print("受伤了")
        self.hp -= value
        if self.hp <= 0:
            self.death()
    def death(self):
        print("死了")



p01 = Defender(50)
d01 = Enemy(100)
d01.damage(d01)






























