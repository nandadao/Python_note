"""
    技能系统
        特征：
            封装：将每种具体影响效果单独定义到类中
            继承：定义影响效果类，统一各种具体影响效果的做法。
                 从而隔离了释放器与具体影响效果的变化。
            多态：每种具体影响效果都是重写影响效果类
                 释放器调用影响效果类 SkillImpactEffect
                 创建具体影响效果(eval("子类名称"))，调用影响方法。
                  DamageEffect     impact
        原则：
            开闭：增加新影响效果，释放器不变。
            单一： 每种影响效果都只负责自己的算法。技能释放器专注于释放技能。
            依赖倒置：技能释放器调用影响效果，没有调用伤害生命、消耗法力等具体做法.
            组合复用：技能释放器 与 影响效果是组合关系，而不是继承关系。
            里氏替换：...
            迪米特：所有类互不影响
        优势：
            外界一个需求的变化，内部只需要修改一个类。【单一职责】
            增加新影响效果，释放器不变。【开闭原则】
            一个技能改变一种影响效果，只需要修改配置文件，代码不用变化。【依赖注入】

"""


class SkillImpactEffect:
    """
        技能影响效果
    """

    def impact(self):
        pass


class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """

    def __init__(self, value=0, duration=0.0):
        self.value = value
        self.duration = duration

    def impact(self):
        super().impact()
        print("扣你%d血" % self.value)


class CostSPEffect(SkillImpactEffect):
    """
        消耗法力效果
    """

    def __init__(self, value=0):
        self.value = value

    def impact(self):
        super().impact()
        print("消耗%d法力" % self.value)


class DizzinessEffect(SkillImpactEffect):
    """
        眩晕效果
    """

    def __init__(self, duration=0):
        self.duration = duration

    def impact(self):
        super().impact()
        print("眩晕%d秒" % self.duration)


class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力效果
    """

    def __init__(self, value=0, duration=0):
        self.value = value
        self.duration = duration

    # 3. 重写
    def impact(self):
        super().impact()
        print("降低%d秒防御力" % self.duration)


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
            "六脉神剑": ["DamageEffect(50,6)"],
            "降龙十八掌": ["DamageEffect(200,18)", "DizzinessEffect(8)"],
            "小无相功": ["DamageEffect(200,18)", "LowerDeffenseEffect(0.5,10)", "CostSPEffect(30)"],
        }

    def __create_effect_object(self):
        list_effect_names = self.__config_file[self.name]
        effect_objects = []
        for item in list_effect_names:
            # 2. 创建子类对象
            # "DamageEffect(50,6)" --> DamageEffect(50,6)
            obj = eval(item)
            effect_objects.append(obj)
        return effect_objects

    def generate_skill(self):
        print(self.name, "释放啦")
        for item in self.__effect_objects:
            # 1. 调用父类方法
            item.impact()


lmsj = SkillDeployer("六脉神剑")
lmsj.generate_skill()

xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()












