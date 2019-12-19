
# 分离对话内容

# 存储说话的人　{name:["abc", "def聊天内容"]}
person = {}

f = open("talk.txt", "r")
for line in f:
    if line != "\n":   #　如果不是空行
        role, line_spoken = line.split("：", 1)  #　只切割第一个冒号
        if role not in person:
            person[role] = [line_spoken]
        else:
            person[role].append(line_spoken)

f.close()

for name in person:
    with open(name+".txt", "w") as fw:
        fw.writelines(person[name])





















