"""
    根据面向对象思想，描述下列情景。
        玩家攻击敌人，敌人受伤(减血,加分)后可能死亡(掉落装备)。
        敌人攻击玩家，玩家受伤(减血,碎屏)后可能死亡(游戏结束)。
        [核心：行为的不同，使用类区分。]
"""

class Player:
    def __init__(self, hp=0,atk = 0):
        self.atk = atk
        self.hp = hp

    def attack(self,target):
        target.damage(self.atk)

    def damage(self,value):
        print("减血")
        print("碎屏")
        self.hp -= value
        if self.hp <=0:
            self.death()

    def death(self):
        print("游戏结束")


class Enemy:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def attack(self,target):
        target.damage(self.atk)

    def damage(self,value):
        self.hp -= value
        print("敌人扣血")
        print("给玩家加分")
        if self.hp <=0:
            self.death()

    def death(self):
        print("死亡")
        print("掉落装备")


p01 = Player(99999,50)
e01 = Enemy(100,10)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)









