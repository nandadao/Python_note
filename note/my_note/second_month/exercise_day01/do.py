
def tell_kuohao(file_addr):
    f = open(file_addr, "r")
    data = f.read()  # 这是带有括号的一大段字符串
    for item in data:  # item是每一个字符
        # if item == "(":   # 判断字符是否为括号
        #     pass
        # elif item == "[":
        #     pass
        # elif item == "{":
        #     pass
        if item in ["(", "[", "{"]:
            pass




    print(data)
    print(type(data))

    f.close()

tell_kuohao("talk.txt")
