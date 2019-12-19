"""
编写一个函数，传入端口名称，返回
这个端口描述信息中，对应的address值

  * 段与段之前有空行
  * 每段首单词是端口名
"""
import re

def get_address(port):
    f = open("exc.txt")
    while True:
        # 搞到每一段
        data = ""
        for line in f:
            if line == '\n':
                break
            data += line
        # 文件结尾
        if not data:
            return "没有该端口"
        # 获取首个单词
        obj = re.match(r"\S+",data)
        if port == obj.group():
            # 找到目标段
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern =r"(\d{1,3}\.){3}\d{1,3}/\d{1,3}|Unknow"
            obj = re.search(pattern,data)
            if obj:
                return obj.group()
if __name__ == '__main__':
    print(get_address('TenGigE0/0/2/3'))





