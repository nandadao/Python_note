"""

    根据时分 ---> 总秒数
    根据时秒 ---> 总秒数
    根据分秒 ---> 总秒数
    根据分 ---> 总秒数
"""


def hms_to_second(h=0, m=0, s=0):
    return h * 60 * 60 + m * 60 + s


print(hms_to_second(h=1, m=3))
print(hms_to_second(h=1, m=4))
print(hms_to_second(m=4, s=9))
print(hms_to_second(m=3))











