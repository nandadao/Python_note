## 复习

### １．基础概念

１．什么是数据库，为什么使用数据库
２．数据库工作模型：
３．数据库的分类：关系型，非关系，开源不开源，大型小型
４．关系型数据库组织结构：
	　　数据元素　　-->　　记录     　-->　数据表　　--> 　　数据库

### ２．mysql

１．关系型　　开源　　c/c++ 

### ３．SQL语句

１．数据库操作
show databases;
create database  [db_name];
use [db];
select database();
drop database  [db];

２．数据表操作
×　根据业务需求确定存什么　　- > 设计字段　　->  　确定数据类型
×　数字类型：数字：tinyint  int float decimal
							  字符串：char   varchar  text  blob  set  enum
×　字段约束：unsigned无符号类型
							   primary key   -- > auto_increment   （设置主键，并且设置为自增长）
							   null (默认是可以为空)     /   not null 
						      default 　[value]

×　show tables;
		create  table [tb_name]   (字段1　类型,字段2  类型 约束,...  );
	    desc　[tb_name];
		drop  table  [db_name];

３．增删改查

insert into  [tb_name]  [col1 ...]  values  (),();
select   [*/col] from [tb] [where];
update  [tb] set [col=value] [where...];
delete from  [tb] [where];

where 子句
	　　算术　　逻辑　　　比较

```
１．熟练掌握sql：创建数据库，创建数据表，增删改查语句

２．创建数据库books，
		创建数据表book
		表字段如下：
		id author price publicat

插入若干数据，７－８条数据
price:　30-80
出版社：中国教育，机械工业，人民教育，

查找练习：
		１．查找所有价格３０多的书
		２．查找出版社为中国教育的出版社的
		３．查找老舍写的中国教育出版社的
		４．查找备注不为空的
		５．查找价格大于６０的，只看书名和价格
		６．查找钱钟书或莫言的书
				where  author  in   ("钱钟书","莫言");
```

```mysql
create talble book (id int primary key auto_increment,);

insert into book values (1,"骆驼祥子","老舍",46.8,"中国教育出版社","写的不错");

```

##  新知识

### １．表字段操作

１．增加字段（add）　
alter  talbe 表名　add  字段名　数据类型;
alter table interest add email char(28);

２．删除字段（drop）
alter table 表名　drop  字段名;

３．修改数据类型（modify）
alter table 表名　modify 　字段名　新数据类型;

４．修改字段名（change）
alter table 表名　change  旧字段名　新字段名　新数据类型;
alter table interest change remark comment text;

５．表名命名（rename）
alter table 表名　rename 新表名;

### ２．时间类型数据

１．

２．时间操作：
(now()  -   interval  7 day);  其中interval 是关键字

### 练习

１．将某一本书的价格修改为４５
２．增加一个字段为出版日期，类型为date
３．将骆驼祥子的出版日期定为2012-1-16
４．将呐喊的出版日期定为1999-10-1
５．删除2000年前出版的图书

### ３．高级查询语句

１．模糊查询和正则查询
like
select * from cls where name like "A%";　查找名字是A开头的
select * from cls where name like "___";　查找名字有三个字符的Tom

正则
select * from cls where name regexp "^A.+";　选出姓名以A开头的

### ４．as用法

１．

### ５．排序

１．order by

### ６．分页(限制)

１．update cls set score = 93 where sex = "m" limit 1;只修改第一个

### ７．联合查询

１．select * from cls where score >= 90 union all select * from cls where age > 18;
就是把union两侧查询出的结果拼接在一起，有没有all默认去重，有all全部显示，不管是否重复。

### ８．子查询

１． from 之后 ，此时子查询的内容作为一个新的表内容，再进行外层select查询
select name from (select * from class_1 where sex='m') as s where s.score > 90;

２．

### 练习

１．创建表　sanguo
create table sanguo (id int primary key auto_increment,name varchar(30),gender enum("男","女"),country enum("魏","蜀","吴"),attack smallint,defense tinyint);

２．表结构如下：            性别 	   	　　	　　　攻击力　　　　防御力
	　　id 　　name 　　gender       country　　attack(>100)　defense(0-100)

３．插入数据使用图形化，插入
		魏：　司马懿　夏侯渊　张辽　曹操　甄姬
		蜀：　赵云　　孙尚香　诸葛亮　张飞　关羽
		吴：　周瑜　　小乔　　大乔　陆逊　鲁肃

４．查找所有蜀国人信息
select * from sanguo where country = "蜀";

​		将赵云的攻击力设为360，防御力设置为68
update sanguo set attack = 360,defense=68  where name="赵云";

​		将吴国英雄攻击力超过300的　改为300,防御力改为65
update sanguo set attack = 300,defense=65 where country = "吴" and attack >= 300;

​		查找攻击力高于250的蜀国英雄的名字和攻击力
select name,attack from sanguo where country = "蜀" and attack>250;

​		将所有英雄攻击力按照从高到底排名，如果攻击力相同按照防御力从高到底排名
select * from sanguo order by attack desc,defense desc;

​		将魏蜀两国英雄名字为三个字的按照防御力升序排序
select * from sanguo where country in ("魏","蜀") and name like "___" order by defense;

​		找到吴国英雄中攻击力排名前2的
select * from sanguo where country = "吴" order by attack desc limit 2;

​		找蜀国中攻击力大于魏国攻击力最高的英雄
select * from sanguo where country = "蜀" and attack > (select attack from sanguo where country = "魏" order by attack desc limit 1);

### ９．聚合操作

１．函数select avg(attack),sum(attack) from sanguo where country = "蜀";

２．分组

３．筛选

４．去重

５．运算

### １０．索引操作

１．索引：数据量小的时候不要索引，写的多的不要索引
２．索引分类：
		普通索引()

=======================================

### 作业:

１．熟练掌握：高级查询，聚合查询，索引查询
２．上网查一下：数据结构　　《数据结构与算法python语言结构》
３．









































