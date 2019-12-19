"""
    使用面向对象思想,描述下列情景:
        防守者攻击敌人,敌人受伤,还能死亡.
"""

class Defender:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self, target):
        print("揍你")
        target.damage(self.atk)

class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        print("呃,受伤了")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("死啦")

d01 = Defender(50)
e01 = Enemy(10)
d01.attack(e01)
print(e01.hp)
d01.attack(e01)
print(e01.hp)