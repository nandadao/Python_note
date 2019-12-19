"""
写出判断一个字符串是否是回文的算法.
   上海自来水来自海上
"""
message = "上海自来水来自海上"
if message == message[::-1]:
    print("是回文")
else:
    print("不是回文")