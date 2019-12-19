"""
１．通过程序描述登录注册过程，将其各封装为一个函数
def login(name,passwd):
				pass
def  register(name,passwd):
				pass
"""
"""
假设:数据库
User   --> user   id  name  passwd
db　数据库对象
"""


# 注册账号
def register(name, passwd):
    # 判断用户名是否重复
    sql = "select name from user where name = '%s'"%name
    cur.excetue(sql)
    result = cur.fetchone()  # 查不到返None
    if result:
        return False
    try:
        sql = "insert into user (name,passwd) values (%s,%s);"
        cur.excetue(sql,[name,passwd])
        db.commit()
        return True
    except:
        db.rollback()
        
        return False


# 登录账号
def login(name, passwd):
    sql = "select name from user where name='%s' and passwd = '%s'"
    cur.execute(sql,[name,passwd])
    result = cur.fetchone()  # 如果查到了说明存在
    if result:
        return True
    else:
        return False
    # 判断用户名是否在数据库

    # 如果有，再对比密码是否正确

    # 如果名字和密码都正确　则可以登录
    pass




