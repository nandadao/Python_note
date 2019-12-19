"""
    体会三大设计原则

    需求：
        1.创建手雷类，定义爆炸方法。
        2.当爆炸时，有可能伤害敌人，玩家，。。。
        3.需求变化：
            房子、树、鸭子、(需要封装)

    目的：通过案例，
    1.先画图，老张开车去东北
    2.
"""


# 老师的答案
class Grenade:
    def __init__(self, atk=0):
        self.atk = atk

    def explode(self, target):
        print("爆炸")
        target.damage(self.atk)


class Damageable:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        """
            受伤的逻辑
        :param value:需要伤害的量
        """
        pass


# --------------------以上是架构师的结果

class Player(Damageable):

    def damage(self, value):
        print("玩家受伤了")


class Enemy(Damageable):

    def damage(self, value):
        print("敌人受伤了")


# ------------------下面是测试代码
g01 = Grenade(50)
p01 = Player()
p01.damage(100)

# 封装：分
# 继承：隔
# 多态：做

# 原则
#   开闭
#   依赖倒置


# class Bomb:
#     def damage(self, obj):
#         print("手雷爆炸")
#         obj.harm()
#
#
# class Obj:
#     def harm(self):
#         pass
# # -------------------------------------------
#
#
# class Room(Obj):
#     def harm(self):
#         print("房子受损")
#
#
# class Tree(Obj):
#     def harm(self):
#         print("树木受损")
#
#
# class Duck(Obj):
#     def harm(self):
#         print("鸭子熟了")
#
#
#
# b01 = Bomb()
# r01 = Room()
# b01.damage(r01)
# t01 = Tree()
# b01.damage(t01)
