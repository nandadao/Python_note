"""
练习：
创建数据库 dict
数据库中创建数据表　words 包含三个字段
id   word    mean
将dict.txt中的单词插入到这个数据库，插入结果必须在98%以上为成功
192300条记录算成功
"""

import pymysql
import re

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

# 生成游标对象　（操作数据库执行sql语句获取结果的对象）
cur = db.cursor()


f = open("dict.txt","r")
args_list = []
for line in f:
    # 获取单词和解释
    result = re.findall(r"(\S+)\s+(.*)", line)   # 正则结果： [("word","mean"),...]
    args_list.extend(result)  # 合并为一个列表
f.close()

# 方法２

# for line in f:
#     # tmp = line.split(' ',1)
#     # word = tmp[0]
#     # mean = tmp[1].strip()
#     # cur.execute(sql,[word,mean])
#
#     tup = re.findall(r'(\S+)\s+(.*)',line)[0]
#     cur.execute(sql, tup)




sql = "insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql,args_list)
    db.commit()
except:
    db.rollback()






# 关闭游标和数据库
cur.close()
db.close()
















