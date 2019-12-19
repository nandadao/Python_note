"""
3. (扩展)一个小球从100米高度落下，
   每次弹回原高度一半。
   请计算：
   -- 总共弹起来多少次(最小弹起来的高度0.01m)。
   -- 整个过程经过多少米。
"""
# 数据
height = 100
count = 0
distance = height
# 算法
while height / 2 > 0.01:
    height /= 2
    count += 1
    distance += height * 2# 累加起/落距离
    # print("第%d次弹起来的高度是%f"%(count,height))
print(count)
print(distance)


