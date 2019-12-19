"""
    读数据库
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
# name = input("name：")
# 组合sql语句
# sql = "select name,hobby from interest where name = '%s';"% name
# print(sql)


sql = "select name,age from cls where age> %s or sex = %s;"
cur.execute(sql,[17,"m"])

# 获取查询结果
# 遍历游标，cur是一个迭代器，所以可以通过for取值
# for i in cur:
#     print(i)

# 获取一个查询结果
# print(cur.fetchone())
# 获取多个查询结果
# print(cur.fetchmany(2))
# 获取所有查询结果
print(cur.fetchall())  # 返回的格式是元组里套元组



# 关闭游标和数据库
cur.close()
db.close()





















