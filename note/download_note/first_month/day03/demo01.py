"""
    行
"""
# 4个物理行 对应 4个逻辑行
number01 = 10
number02 = 50
result = number01 + number02
print(result)

# 2个物理行 对应 4个逻辑行（不建议）
number01 = 10;
number02 = 50;
result = number01 + number02
print(result)

# 3个物理行 对应 1个逻辑行
number01 = 1 + \
           2 + 3 + 4 \
           + 5 + 6
# 括号天然的换行符
number01 = 1 + (2 +
                3 + 4
                + 5) + 6