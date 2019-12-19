
# 导入模块成功的唯一条件：
# sys.path + 导入路径 可以正确定位模块

import sys

sys.path.append('/home/tarena/month01/day15/my_project')
print(sys.path)


from common.list_helper import ListHelper



class SkillDeployer:
    def generate_skill(self):
        print("SkillDeployer -- generate_skill")


ListHelper.fun01()