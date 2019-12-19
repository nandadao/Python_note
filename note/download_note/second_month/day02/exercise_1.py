"""
练习 ： 编写一个程序，从终端使用input输入一个单词，打印出这个单词及其解释
       * 每个单词一行
       * 单词和解释之间有空格
       * 单词按照升序（从小到大）排列
"""
word = input("单词:")  # 要查找单词

f = open('dict.txt') # 文本方式打开

# 每次获取一行
for line in f:
    w = line.split(' ')[0]
    if w > word:
        print("没有该单词")
        break
    elif word == w:
        # 查到单词
        print(line)
        break
else:
    print("没有该单词")

f.close()










