class Person:
    高大 = False
    威猛 = False
    温柔 = False
    善良 = False
    有钱 = False
    聪明 = False


qtx = Person()
qtx.有钱 = True
qtx.聪明 = True


class Person:
    特征 = 0
    高大 = 1
    威猛 = 2
    温柔 = 4
    善良 = 8
    有钱 = 16
    聪明 = 32


qtx = Person()
qtx.特征 = 48

# if qtx.特征 & 温柔

qtx.特征 = qtx.特征 | qtx.善良 # 添加善良
print(qtx.特征 )


















