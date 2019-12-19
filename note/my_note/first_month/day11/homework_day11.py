"""
	3. 创建技能类（数据：技能名称,冷却时间,消耗法力,攻击比例）
                          0-60    0-100   0 - 1
"""

# 这是数据的封装?
# class Skill:
# 	def __init__(self, name, time, magic, attack):
# 		self.name = name
# 		self.time = time
# 		self.magic = magic
# 		self.attack = attack
#
# 	@property
# 	def time(self):
# 		return self.__time
# 	@time.setter
# 	def time(self, value):
# 		if 0 <= value <= 60:
# 			self.__time = value
# 		else:
# 			raise Exception("冷却时间输入有误")
#
# 	@property
# 	def magic(self):
# 		return self.__magic
# 	@magic.setter
# 	def magic(self, value):
# 		if 0 <= value <= 100:
# 			self.__magic = value
# 		else:
# 			raise Exception("消耗法力输入有误")
#
# 	@property
# 	def attack(self):
# 		return self.__attack
# 	@attack.setter
# 	def attack(self, value):
# 		if 0 <= value <= 1:
# 			self.__attack = value
# 		else:
# 			raise Exception("攻击比例输入有误")
#
#
# s01 = Skill("大炮", 30, 22, 0.5)
# print(s01.name)
# print(s01.time)
# print(s01.magic)
# print(s01.attack)



"""
	4. 根据面向对象思想，描述下列情景。
   张无忌 教 赵敏九阳神功
   赵敏 教 张无忌玉女心经
   张无忌上班挣了10000元
   赵敏上班挣了8000元
"""

# 我的答案（错的）
# class Person:
# 	def __init__(self, name):
# 		self.name = name
# 		# self.money = money
#
# class Teach:
# 	def __init__(self, skill, person):
# 		self.skill = skill
# 		self.person = person
# 	def teach_skill(self, person, skill):
# 		self.person = person
# 		skills = []
# 		skills.append(skill)
# 		print(self.person,"教",person,self.skill)
#
# class Make_Money:
# 	def make_money(self):
# 		pass
#
#
# p01 = Person("张无忌")
# p02 = Person("赵敏")
# t01 = Teach(p01,"九阳神功")
# t01.teach_skill(p02, t01)

# 老师的答案
# 创建一个类，人的行为，数据不同用对象区分
# class Person:
#     def __init__(self, name=""):
#         self.name = name
#
#     def teach(self, person_other, str_skill, ):
#         print(self.name,"教", person_other.name, str_skill)
#
#     def work(self, money):
#         print(self.name , "上班挣钱", money)
#
#
#
# zwj = Person("张无忌")
# zm = Person("赵敏")
#
# zwj.teach(zm, "太极")
#
# zwj.work(1000)




"""
5. 根据面向对象思想，描述下列情景。
玩家攻击敌人，敌人受伤(减血,加分)后可能死亡(掉落装备)。
敌人攻击玩家，玩家受伤(减血,碎屏)后可能死亡(游戏结束)。
"""
# 我的答案
# class Plsyer:
#     def __init__(self, atk=0):
#         self.atk = atk
#
#     def attack(self, target):
#         print("揍你")
#         target.damage(self.atk)
#
# class Enemy:
#     def __init__(self, hp=0):
#         self.hp = hp
#
#     def damage(self, value):
#         print("呃,受伤了")
#         self.hp -= value
#         if self.hp <= 0:
#             self.death()
#
#     def death(self):
#         print("游戏结束")

# 老师答案
# 核心：行为的不同，用类区分

class Player:
    def __init__(self, atk=0, hp=0):
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        target.damage(self.atk)

    def damage(self, value):
        print("减血")
        print("碎屏")
        self.hp -= value


class Enemy:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def attack(self, target):
        target.damage(self.atk)


    def damage(self, value):
        self.hp -= value
        print("扣血")
        print("玩家加分")
        if self.hp <= 0:
            self.death()

    def death(self):
        print("死亡")
        print("掉落装备")


p01 = Player(50)
e01 = Enemy(100)
p01.attack(e01)
print("----------------------")
p01.attack(e01)
















