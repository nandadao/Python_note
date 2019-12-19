""""""
"""
6行4列
    ****  r1
    ####  r2
    ****
"""
# for r in range(6):
#     for c in range(4):
#         if r % 2 == 0:
#             print("*",end="")
#
#         else:
#             print("#", end="")
#     print()

"""
    外层4行  内层
    *       1
    **      2
    ***     3
    ****    4
"""

for r in range(4):
    for c in range(r+1):
        print("*", end="")
    print()




















