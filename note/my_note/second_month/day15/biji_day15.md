day15

### 复习

１．外键约束
foreign key
表A（主键）----表B(外键)
主表　　　　　从表
一　　　　　　多
constraint [外键名称] foreign key (本表的外键字段) 　references  [主表]　(主表的主键)  on delete cascade on update cascade;

删除外键:alter table [tb] drop foreign key [外键名称]　　　　－－－>然后再删除索引

级连动作：cascade 主表删除
　　　　　restrict 
         　　　set null

２．表关联设计（重点）学会创建
一对一
一对多
多对多

３．表的关联查询
内连接　tb1 inner join tb2 on  [连接条件]
外连接
　左连接　[左表] left join [右表] on [连接条件]－－－－>以左表为主表
　有连接　[左表] right join [右表] on [连接条件]－－－－>以右表为主表

　

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

### 新知识

### １．视图

增删改查视图的时候，要根据原来的表的约束条件，
判断是否为视图：show create table c1;查看结果中有view是视图
　　　　　　　　show full tables in stu where table_type like "VIEW";
删除视图：
drop view [if exists]   c1;　　加上if exists后，如果没有该视图也不会报错

修改视图
参考创建视图，将create关键字改为alter
alter view c1 as select name,age,score from class_1;    select 后面是新的筛选条件
create or replace view c1 as select name,age,score from cls;或者用or　replace替换也行

### ２．函数和存储过程

１．函数必须要有return 　　　（查数据）

mysql> delimiter $$
mysql> create function st1() returns int
    -> begin
    -> update cls set score = 60 where name="Emma";
    -> set @a=(select score from cls where name="Emma");
    -> return @a;
    -> end$$

２．begin和end 之间的语句需要加分号

３．存储过程创建(一定没有返回值)   　（增删改查操作　都可以）

调用方法：call st();   

```mysql
mysql> delimiter $$
mysql> create procedure st()
    -> begin
    -> select name,age from cls;
    -> select name,score from cls order by score desc;
    -> end $$

```

```
函数内变量加减法
mysql> create procedure test(in age int)
    -> begin 
    -> declare val int;
    -> set val=1;
    -> set val=val+age;
    -> select val;
    -> end $$

```

```mysql
into赋值方法
mysql> delimiter $$
mysql> create procedure test2(in uid int) begin  declare val int; select age from cls where id= uid into val;select val; end$$

```

查看当前数据库中所有的存储过程：
mysql> select name from mysql.proc where db="stu" and type="procedure";

练习：

使用cls表完成
编写一个函数，传入两个id,返回连个人的分数之差
自己写：create function score1(sid1 int,sid2 int) returns int begin return (select score from cls where id = sid1) - (select score from cls where id = sid2); end$$

老师：delimiter $$  
 create function st_exc(uid1 int,uid2 int) returns float begin set @val1=(select score from cls where id=uid1); set @val2=(select score from cls where id=uid2); set @r=@val1-@val2; return @; end$$

编写一个存储过程，传入学生id，同时传入一个out类型的变量，通过out类型变量获取这个id学生的学生年龄

```sql
mysql> create procedure get_age(in uid int,out num int)
    -> begin
    -> declare val int;
    -> select age from cls where id=uid into val;
    -> set num=val;
    -> end $$
```

### ３．事物控制   ACID

１．特性（一定要知道）
　　１．原子性
　　２．

２．事务隔离级别（一定要知道）

### ４．数据库优化

１．数据库设计范式

了解前三个范式就行了





### 面试之前回顾，第二阶段１４、５、６天

### 作业：

１．视图，存储过程，函数，事务，语句熟练

２．思考问题：
后台管理，商家，骑手，用户，

如何创建数据库









































