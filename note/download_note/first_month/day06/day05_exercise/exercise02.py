"""
4. 彩票
    双色球
    红色：6个  1--33   不能重复
    蓝色：1个  1--16
    -- 随机产生一注彩票(列表)
"""
import random

list_ticket = []
while len(list_ticket) < 6:
    number = random.randint(1, 33)
    if number not in list_ticket:
        list_ticket.append(number)

list_ticket.append(random.randint(1,17))