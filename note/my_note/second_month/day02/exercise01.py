"""
    练习：
        编写一个程序，从终端使用input输入一个单词，打印出这个单词及其解释
    提示：每个单词占一行
         单词和解释之间有空格
         单词按照升序排列，后面的单词比前面的单词大
"""

f = open("/home/tarena/note/do/dict.txt", "r")


word = input("请输入要查询的单词：")
# for i in f:
#     if i[0:len(word) + 1] == word + " ":
#         print(i)



for line in f:
    w = line.split(" ")[0]
    # print(line.split(" "))
    if w > word:
        print("没有该单词")
        break
    if w == word:
        print(line)
        break

else:
    print("没有该单词")













f.close()
