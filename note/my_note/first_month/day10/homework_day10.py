"""
	    3.以万物皆对象的思想，洞察身边客观存在的事物，
      将其抽象为类，再创建对象。
      （即面向对象思想）
"""

"""
	类：      对象：
	学生      每一个学生
	狗        每一只不同的狗
	树叶      世界上没有相同的两片树叶
	大海       太平洋  大西洋...
	人类       每一个不同的人
	星球       火星  土星  金星...
	车票       每个人手里的车票
	股票       每个人手中的股票
	

	
"""



"""
	4.创建敌人类
       1. (数据：名称，血量，攻击力，防御力)
       2. 行为：打印个人信息
       3.创建敌人列表
       4.在敌人列表中查找“灭霸”对象
       5.再敌人列表中查找所有死人（血量为0）
       6.在敌人列表中赵攻击力最大的敌人
       7.根据。防御力，对敌人列表进行降序排列
"""


class Enemy():
	def __init__(self, name, blood, attack, defense):
		self.name = name
		self.blood = blood
		self.attack = attack
		self.defense = defense
		self.de = de


	def print_info(self):
		print("%s的血量是%d,攻击力是%d,防御力是%d"%(self.name, self.blood, self.attack,self.defense))



list_enemy = [
	Enemy("黑寡妇", 50, 220, 1330),
	Enemy("灭霸", 0, 3320, 130),
	Enemy("钢铁侠", 50, 20, 230),
	Enemy("绿巨人", 50, 120, 430),
]


# 4.找到灭霸
def find_mieba():
	for item in list_enemy:
		if item.name == "灭霸":
			return item

# re = find_mieba()
# if re:
# 	re.print_info()


# 5.再敌人列表中查找所有死人（血量为0）
def find_death():
	list_death = []
	for item in list_enemy:
		if item.blood == 0:
			list_death.append(item)
	return list_death

# re = find_death()
# for i in re:
# 	if i:
# 		i.print_info()


# 6.在敌人列表中赵攻击力最大的敌人
def find_biggest_attack():
	biggest = list_enemy[0]
	for i in range(1, len(list_enemy)):
		if list_enemy[0].attack < list_enemy[i].attack:
			biggest = list_enemy[i]

	return biggest

# find_biggest_defense().print_info()



# 7.根据。防御力，对敌人列表进行降序排列

def defense_big_to_small():
	for r in range(len(list_enemy)-1):
		for c in range(r+1, len(list_enemy)):
			if list_enemy[r].defense < list_enemy[c].defense:
				list_enemy[r], list_enemy[c] = list_enemy[c], list_enemy[r]


# defense_big_to_small()
# for item in list_enemy:
# 	item.print_info()









