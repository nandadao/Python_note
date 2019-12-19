"""
    ２．文件分离练习
​	一个文件，文件名＂talk.txt＂，再文件中保存一些对话信息，格式如下：
​	老王：吃了么
​	老李：没呢，您呢？
​	老张：您二位干什么呢？
​	老李：溜弯啊，刚买菜会啊里啊
​	老张：是啊
通过程序，将该文件进行分离，每个人物的说话内容，重新写入一个新的文件中，文件以这个人的名字命名．
"""


f = open("talk.txt", "r")
print(f)
count = 0
for item in f:  # item = "老李：溜弯啊，刚买菜会啊里啊"
    for i in item:  # i = "老"  item.split("：")[0]
        if i == "：":
            count = item.index(i)
            break
    print(count)
    name = item[0:count]  # 看一下这个count是否不变
    f_name = open(name,"a")
    f_name.write(item+"\n")
    f_name.close()


f.close()





















