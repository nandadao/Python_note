import pymysql

db = pymysql.connect(host=
                     port)

cur = db.cursor()

cur.execute("sql语句")

# 如果是查询的话就用
print(cur.fetchall())
# 或者
for i in cur:
    print(i)

# 如果是写入的话
db.commit()

# 关闭游标和数据库
cur.close()
db.close()




















