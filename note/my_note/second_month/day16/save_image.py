
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

# 文件存储
# f = open("边牧.jpeg","rb")
# data = f.read()
# f.close()
# try:
#     sql = "update cls set image = %s where id =1;"
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()

# 读取文件
sql = "select image from cls where id =1;"
cur.execute(sql)
data = cur.fetchone() # 返回元组，
print(data)
with open("dog.jpeg","wb") as f:
    f.write(data[0])



# 关闭游标和数据库
cur.close()
db.close()














