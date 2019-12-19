"""
    技能系统
        三大特征：
            1.封装:技能释放器、伤害生命效果、消耗发力效果、降低防御力效果、嘲讽效果
            2.继承:技能影响效果
            3.多态:伤害生命效果、消耗发力效果、降低防御力效果、嘲讽效果,四种效果不同
        六大原则：
                开闭：增加新技能影响，不改变技能释放器
                单一：员伤害生命效果(扣血)、消耗发力效果(减少法力)、降低防御力效果(降低防御力)、嘲讽效果(嘲讽)
                     每种影响效果只负责自己的算法，技能释放器专注于技能释放器
                依赖倒置：技能释放器，调用技能影响效果而不调用具体影响

                组合复用：技能释放器和技能影响是组合关系

                里氏替换：（有父的地方，传子类对象）这里没有体现
                迪米特：技能释放器、与  伤害生命效果、消耗发力效果、降低防御力效果、嘲讽效果，互不影响

        优势：高内聚、低耦合、使用eval()可以通过配置文件进行运行代码、
             # 老师
             1.外界一个需求的变化，内部只需要修改一个类（单一职责）
             2.增加新的影响效果，释放器不变（开闭原则）
             3.一个技能改变一种影响效果，只需要修改配置文件，代码不用变化（依赖注入）



















"""


class SkillImpactEffect:
    """
        技能影响效果
    """
    def impact(self):
        pass


class DamageEffact(SkillImpactEffect):
    """
        伤害生命效果
    """

    def __init__(self, value=0, duration=0):
        self.value = value
        self.duration = duration

    def impact(self):
        super().impact()
        print("扣你%d血%d次"%(self.value, self.duration))

class CosSPEffact(SkillImpactEffect):
    """
        消耗发力效果
    """

    def __init__(self, value=0):
        self.value = value

    def impact(self):
        super().impact()
        print("消耗%d法力"%self.value)


class DizzinessEffact(SkillImpactEffect):
    """
        嘲讽效果
    """

    def __init__(self, duration=0):
        self.duration = duration

    def impact(self):
        super().impact()
        print("眩晕%d秒"%self.duration)


class LowerDeffenseEffact(SkillImpactEffect):
    """
        降低防御力效果
    """

    def __init__(self, value, duration=0):
        self.value = value
        self.duration = duration

    def impact(self):
        super().impact()
        print("降低%d防御力"%self.value)

class SkillDeployer:
    """
        技能释放器
    """
    def __init__(self, name=""):
        self.name = name
        self.__config_file = self.__load_config_file()
        self.__effect_objects = self.__create_effect_object()

    def __load_config_file(self):
        return {
            "太极": ["DamageEffact(50,6)"],
            "降龙十八掌": ["DamageEffact(200,18)", "DizzinessEffact(8)"],
            "小无相功": ["DamageEffact(200,18)", "LowerDeffenseEffact(0.5, 10)", "CosSPEffact(30)"],
        }

    def __create_effect_object(self):
        list_effect_names = self.__config_file[self.name]
        effect_objects = []
        for item in list_effect_names:
            obj = eval(item)
            effect_objects.append(obj)
        return effect_objects

    def generate_skill(self):
        print(self.name , "释放了")
        for item in self.__effect_objects:
            item.impact()


xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()






























