"""
    mysql.py
    pymysql　数据库操作
"""
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 生成游标对象　（操作数据库执行sql语句获取结果的对象）
cur = db.cursor()

# 利用游标对象执行各种sql语句　
# 如果执行的是读操作-->用fetch
# 写操作　　　　　--> commit    rollback
# cur.execute()

# 关闭游标和数据库
cur.close()
db.close()


















