"""
    ### 练习：
编写一个函数，传入端口名称，返回这个端口描述信息，对应的addredss值
提示：
１．段与段之间有空行
２．每段首单词是端口名
"""
import re


def get_address(port):
    f = open("exc.txt", "r")
    while True:
        # 搞到每一段
        data = ""
        for line in f:
            if line == "\n":
                break
            data += line
        # 文件结尾
        if not data:
            return "没有该端口"
        # 获取首单词
        obj = re.match(r"\S+", data)
        if port == obj.group():
            # 找到目标段
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern = r"(\d{1,3}\.){3}"
            obj = re.search(pattern, data)
            if obj:
                return obj.group()


    #
    # data = f.read()
    # l = re.findall(r"[A-Z]+.+\\r", data, flags=re.DOTALL)
    # print(l)




if __name__ == '__main__':
    print(get_address("BVI100"))



















