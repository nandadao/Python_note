"""
空洞文件
"""
f = open('file','wb')
f.write(b'START')
# 末尾向后移动了10M
f.seek(1024*1024*10,2)
f.write(b'END')

f.close()

