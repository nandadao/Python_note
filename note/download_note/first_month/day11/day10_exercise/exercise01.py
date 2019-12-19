"""
4. 创建敌人类
    -- 数据:名称,血量,攻击力,防御力
    -- 行为:打印个人信息
    -- 创建敌人列表
    -- 在敌人列表中查找"灭霸"对象
    -- 在敌人列表中查找所有死人
    -- 在敌人列表中查找攻击力最大的敌人
    -- 根据防御力,对敌人列表进行降序排列.
"""


class Enemy:
    """
        抽象的敌人
    """

    def __init__(self, name, hp, atk=0, defense=0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def print_self(self):
        print(self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("灭霸", 5000, 900, 200),
    Enemy("悟空", 4700, 1000, 300),
    Enemy("八戒", 8000, 300, 800),
    Enemy("沙僧", 3000, 500, 100),
    Enemy("唐僧", 0, 100, 50),
]


def find01():
    for item in list01:
        if item.name == "灭霸1":
            return item


re = find01()
if re: re.print_self()


def find02():
    list_result = []
    for item in list01:
        if item.hp == 0:
            list_result.append(item)
    return list_result


for item in find02():
    item.print_self()


# -- 在敌人列表中查找攻击力最大的敌人
def find03():
    max_value = list01[0]
    for i in range(1, len(list01)):  # 1 2 3 ..
        if max_value.atk < list01[i].atk:
            max_value = list01[i]
    return max_value


re = find03()
re.print_self()


# -- 根据防御力,对敌人列表进行降序排列.
def sort():
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r].defense < list01[c].defense:
                list01[r], list01[c] = list01[c], list01[r]


sort()
for item in list01:
    item.print_self()
