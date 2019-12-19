### 复习

１．视图
优点：操作方便，数据处理安全性高
缺点：操作效率不高
create [or replace ]view [view_name]  as  [select]　创建视图
drop view [if exists ] view 删除视图
alter [or replace ]view [view_name]  as  [select] 修改视图

２．函数和存储过程
作用：封装
区别：函数一定有返回值，只有in类型参数，目的是获取一个只，里面多用查找
　　　存储过程没有返回值，（语句的集合）参数in  out   inout  ，
　　　参数：in外部
　	　　　　out 里面改
　　　　　　inout包含上面两个

```mysql
函数创建
delimiter [符号]
create function  [f_name](args returns [r_type]
begin
		sql语句
		return val
end  [符号]
delimiter ; 
```

```mysql
存储过程创建
delimiter [符号]
create procedure  [p_name](args
begin
		sql语句
		return val
end  [符号]
delimiter ; 
```

３．事务
概念：一个数据操作的完整过程
四大特性：１．原子性　２．一致性　３．隔离性　４．持久性
隔离性：读未提交
　　　　读已提交
　　　　可重复读
　　　　串行化
begin;　　　commit;　　　rollback;

４．数据库优化

* 数据库范式
* 数据库引擎
* 字段数据及类型选择：占用空间小的高于占用大的，char优于varchar(),数字类型优于日期优于字符串
* 键的设置



＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

## day16笔记

数据库优化

### １．explain语句

一般查找过程type :要是range以上

### ２．SQL优化

### ３．表的复制

```
创建一个hobby表，算是复制select 后面的表
删除hobbby表中的数据，不会影响原表数据
mysql> create table hobby select s.name,s.age,i.hobby from cls as s,interest as i where s.name =i.name;
```

### ４．数据备份

１．备份命令格式
mysqldump -u root -p stu > stu.sql　　：在命令行执行（不是sql语句）

２．恢复数据库
mysql -u root -p student < stu.sql   ：在命令行执行

### ５．用户权限管理

１．开启MySQL远程连接

```
１．sudo su
２．cd /etc/mysql/mysql.conf.d
３．cp mysqld.cnf mysqld.cnf.bak　　备份文件，防止文件出错
４．.vi mysqld.cnf #找到44行左右,加 # 注释
５．保存退出
６．service mysql restart
７．修改用户表host值
 　　use mysql;
　　update user set host='%' where user='root';
８．刷新权限
 　　flush privileges;
```

２．添加授权用户

```mysql
1. 用root用户登录mysql mysql -uroot -p123456
2. 添加用户 % 表示自动选择可用IP CREATE USER 'username'@'host' IDENTIFIED BY 'password
mysql> create user "vip"@"%" identified by "123";
3. 授权
 grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
 grant all privileges on books.* to 'duty'@'%' identified by '123' with grant option;
 4. 刷新权限
 flush privileges;
```

### ６．pymysql使用

１．pymysql使用流程

```mysql
1.db = pymyslq.connect()　建立数据库连接
2.cur = db.cursor()　创建游标对象
3.cur.execute("sql语句")　游标方法，要执行的语句
4.提交到数据库或者获取数据：db.commit()   /   db.fetchall()
5.关闭游标对象：cur.close()
6.断开数据库连接：db.close()
```

２．对数据库进行读操作

```python
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
```

３．对数据库进行写操作

```python
    # 通过executemany执行大量sql语句
    list_ = [(17,1),(18,3),(19,4)]
    sql = "update cls set score = score -5,age= %s where id = %s;"
    cur.executemany(sql, list_)
```

练习：
创建数据库 dict
数据库中创建数据表　words 包含三个字段
id   word    mean
将dict.txt中的单词插入到这个数据库，插入结果必须在98%以上为成功
１９２３００条记录算成功

delete from words;　　删除表内的所有数据

### ７．存二进制文件

１．图片、视频、音频　都是二进制存储形式

２．静态文件存储方法：

* 存储文件所在路径　（varchar）（存储常常改变的数据，广告，视频存在服务器）

    优点：节省数据库空间
    缺点：文件并不在数据库中，如果发生变化可能导致文件丢失

* 存储文件本身　(blob)　　（存储不太发生变化的，文件不会太大，头像，不存视频）
    优点：文件安全
    缺点：文件在数据库中读写效率低

### 练习：登录与注册

１．通过程序描述登录注册过程，将其各封装为一个函数
def login(name,passwd):
				pass

def  register(name,passwd):
				pass

==========================================================

### 作业：

１．总结数据库的内容

２．明天讲项目开发流程git

3.注册一个账号 github.com 明天用















