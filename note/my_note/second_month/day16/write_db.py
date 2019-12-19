"""
    数据库写操作
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
try:
    # 插入操作
    # sql = "insert into cls values (9,'Jammy',21,'m',73);"
    # cur.execute(sql)
    # sql = "insert into cls values (%s,%s,%s,%s,%s);"
    # cur.execute(sql, [10, "Kang", 19, "m", 88])

    # 修改操作
    # sql = "update cls set score = 84 where id = 3;"
    # cur.execute(sql)

    # 删除操作
    # sql = "delete from cls where id = 2;"
    # cur.execute(sql)

    # 通过executemany执行大量sql语句
    list_ = [(17,1),(18,3),(19,4)]
    sql = "update cls set score = score -5,age= %s where id = %s;"
    cur.executemany(sql, list_)

    db.commit()  # 提交结果，立即刷新缓冲区把数据写入数据库
except Exception as e:
    print(e)
    db.rollback()  # 回滚,没有写入数据库的操作召回

# 关闭游标和数据库
cur.close()
db.close()
