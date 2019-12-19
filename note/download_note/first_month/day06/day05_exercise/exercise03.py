"""
    -- 在终端中购买一注彩票
         “请输入第1个红球号码:”
         "号码超过范围"
         “号码已经存在”
"""
list_ticket = []
while len(list_ticket) < 6:
    number = int(input("请输入第%d红球号码：" % (len(list_ticket) + 1)))
    if number in list_ticket:
        print("已经存在")
    elif number < 1 or number > 33:
        print("号码超过范围")
    else:
        list_ticket.append(number)

while len(list_ticket) < 7:
    number = int(input("请输蓝球号码：" ))
    if number < 1 or number > 16:
        print("号码超过范围")
    else:
        list_ticket.append(number)

print(list_ticket)