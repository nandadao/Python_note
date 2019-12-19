### mysql知识总结　　时间2019-12-18

1.数据库操作

```mysql
数据库操作
1.查看已有库
show databases;
2.创建库
create database 库名 [character set utf8]
e.g. 创建stu数据库，编码为
utf8 create database stu character set utf8; 
create database stu charset=utf8;
3.查看创建库的语句
show create database 库名;
4.查看当前所在库
select database();
5.切换库
use 库名;
6.删除库
> drop database 库名;

7.库名的命名规则

> - 数字、字母、下划线,但不能使用纯数字
> - 库名区分字母大小写
> - 不能使用特殊字符和mysql关键字
```

2.数据表操作

```mysql
1.创建表
> create table 表名(
> 字段名 数据类型,
> 字段名 数据类型,
> ...
> 字段名 数据类型
> );
e.g.  创建班级表
create table class_1 (id int primary key auto_increment,name varchar(32) not null,age tinyint unsigned not null,sex enum('w','m'),score float default 0.0);

2.查看数据表
> show tables；

3.查看已有表的字符集
> show create table 表名;

4.查看表结构
> desc 表名;

5.删除表
> drop table 表名;
```

3.数据操作基础

```mysql
1.插入数据  插入(insert)
insert into 表名 values(值1),(值2),...;
insert into 表名(字段1,...) values(值1),...;
e.g. 
insert into class_1 values (2,'Baron',10,'m',91),(3,'Jame',9,'m',90);

2.查询数据  查询(select)
select * from 表名 [where 条件];
select 字段1,字段2 from 表名 [where 条件];
e.g. 
select * from class_1;
select name,age from class_1;

3.更新表记录(update)
update 表名 set 字段1=值1,字段2=值2,... where 条件;
注意:update语句后如果不加where条件,所有记录全部更新
e.g.
update class_1 set age=11 where name='Abby';

4.删除表记录（delete）
delete from 表名 where 条件;
注意:delete语句后如果不加where条件,所有记录全部清空
e.g.
delete from class_1 where name='Abby';

5.表字段的操作(alter)
语法 ：alter table 表名 执行动作;
* 添加字段(add)
    alter table 表名 add 字段名 数据类型;
    alter table 表名 add 字段名 数据类型 first;
    alter table 表名 add 字段名 数据类型 after 字段名;
* 删除字段(drop)
    alter table 表名 drop 字段名;
* 修改数据类型(modify)
    alter table 表名 modify 字段名 新数据类型;
* 修改字段名(change)
    alter table 表名 change 旧字段名 新字段名 新数据类型;
* 表重命名(rename)
    alter table 表名 rename 新表名;
e.g. 
alter table interest add tel char(11) after name;   
```

4.高级查询语句

```mysql
1.使用 LIKE 子句从数据表中读取数据的通用语法：
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 LIKE condition1
e.g. 
mysql> select * from class_1 where name like 'A%';

2.mysql中对正则表达式的支持有限，只支持部分正则元字符
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 REGEXP condition1
e.g. 
select * from class_1 where name regexp '^B.+';

3.as 用法
在sql语句中as用于给字段或者表重命名
select name as 姓名,age as 年龄 from class_1;
select * from class_1 as c where c.age > 17;

4.排序
使用 ORDER BY 子句将查询数据排序后再返回数据
SELECT field1, field2,...fieldN from table_name1 where field1
ORDER BY field1 [ASC [DESC]]
默认情况ASC表示升序，DESC表示降序
select * from class_1 where sex='m' order by age;

5.分页(限制)
LIMIT 子句用于限制由 SELECT 语句返回的数据数量 或者 UPDATE,DELETE语句的操作数量
SELECT column1, column2, columnN 
FROM table_name
WHERE field
LIMIT [num]

6.联合查询
UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中。多个 SELECT 语句会删除重复的数据。
UNION 操作符语法格式：
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL | DISTINCT]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
e.g.
select * from class_1 where sex='m' UNION ALL select * from class_1 where age > 9;

7.子查询
> 定义 ： 当一个select语句中包含另一个select 查询语句，则称之为有子查询的语句
> 子查询出现的位置：
> 1. from 之后 ，此时子查询的内容作为一个新的表内容，再进行外层select查询
select name from (select * from class_1 where sex='m') as s where s.score > 90;
需要将子查询结果集重命名一下，方便where子句中的引用操作
> 2.where字句中，此时select查询到的内容作为外层查询的条件值
 select *  from class_1 where age = (select age from class_1 where name='Tom');
 子句返回的结果需要一个明确值，即需要时某个记录的某个元素，不能是多行或者多列
```

5.聚合操作
聚合操作指的是在数据查找基础上对数据的进一步整理筛选行为，在认识聚合之前先看一个更完整的sql语句

```mysql
select语句执行顺序
(7)     SELECT 
(8)     [DISTINCT] <select_list>
(1)     FROM <left_table>
(3)     <join_type> JOIN <right_table>
(2)     ON <join_condition>
(4)     WHERE <where_condition>
(5)     GROUP BY <group_by_list>
(6)     HAVING <having_condition>
(9)     ORDER BY <order_by_condition>
(10)    LIMIT <limit_number>

1.聚合函数
方法             功能
avg(字段名)   该字段的平均值
max(字段名)   该字段的最大值
min(字段名)   该字段的最小值
sum(字段名)   该字段所有记录的和
count(字段名) 统计该字段记录的个数

2.聚合分组
group by
给查询的结果进行分组
e.g.  : 计算每个国家的平均攻击力
select country,avg(attack) from sanguo group by country;
e.g. :  对多个字段创建索引，此时多个字段都相同时为一组
select age,sex,count(*) from class1 group by age,sex;
e.g. : 所有国家的男英雄中 英雄数量最多的前2名的 国家名称及英雄数量
select country,count(id) as number from sanguo 
where gender='M' group by country
order by number DESC
limit 2;
使用分组时select 后的字段为group by分组的字段和聚合函数，不能包含其他内容。group by也可以同时依照多个字段分组，如group by A，B 此时必须A,B两个字段值均相同才算一组。

3.聚合筛选
having语句
对分组聚合后的结果进行进一步筛选
eg1 : 找出平均攻击力大于105的国家的前2名,显示国家名称和平均攻击力
select country,avg(attack) from sanguo 
group by country
having avg(attack)>105
order by avg(attack) DESC
limit 2;
注意
> - having语句通常与group by联合使用。
> - having语句存在弥补了where关键字不能与聚合函数联合使用的不足,where只能操作表中实际存在的字段,having操作的是聚合函数生成的显示列

4.去重语句
- distinct语句
不显示字段重复值
eg1 : 表中都有哪些国家
  select distinct name,country from sanguo;
eg2 : 计算一共有多少个国家
  select count(distinct country) from sanguo;
  注意
> - distinct和from之间所有字段都相同才会去重

5.聚合运算
- **查询表记录时做数学运算**
运算符 ： +  -  *  /  %  
eg1: 查询时显示攻击力翻倍
  select name,attack*2 from sanguo;
eg2: 更新蜀国所有英雄攻击力 * 2
  update sanguo set attack=attack*2 where country='蜀国';
```

6.索引操作

```mysql
- 定义
索引是对数据库表中一列或多列的值进行排序的一种结构，使用索引可快速访问数据库表中的特定信息。
- **优点**
  ​		加快数据检索速度,提高查找效率
  - **缺点**
  > 占用数据库物理存储空间
  > 当对表中数据更新时,索引需要动态维护,降低数据写入效率
  
1.索引分类
- 普通(MUL) 
> 普通索引 ：字段值无约束,KEY标志为 MUL
- 唯一索引(UNI)
> 唯一索引(unique) ：字段值不允许重复,但可为 NULL,KEY标志为 UNI
- 主键索引（PRI）
> 一个表中只能有一个主键字段, 主键字段不允许重复,且不能为NULL，KEY标志为PRI。通常设置记录编号字段id,能唯一锁定一条记录 

2.索引创建
主键索引的创建方法已经在数据表中介绍过了，下面是普通索引和唯一索引的创建方法：
- 创建表时直接创建索引
create table 表名(
字段名 数据类型，
字段名 数据类型，
index(字段名),
index(字段名),
unique(字段名)
);
在已有表中创建索引
create [unique] index 索引名 on 表名(字段名);

3.查看索引
1、desc 表名;  --> KEY标志为：MUL 、UNI。
2、show index from 表名;

4.删除索引
drop index 索引名 on 表名;

5.已有表添加主键索引或自增长属性
alter table 表名 add primary key(id);
alter table 表名 modify id int auto_increment;

6.创建复合主键
primary key（uid,pid）
此时两个字段只要不都相同即可

7.删除主键索引或自增长属性
alter table 表名 modify id int;  要先删除自增长，因为它只作用于主键字段
alter table 表名 drop primary key;
```

7.外键约束和表关联关系

```mysql
约束 : 约束是一种限制，它通过对表的行或列的数据做出限制，来确保表的数据的完整性、唯一性
foreign key 功能 : 建立表与表之间的某种约束的关系，由于这种关系的存在，能够让表与表之间的数据，更加的完整，关连性更强，为了具体说明创建如下部门表和人员表

1.foreign key 外键的定义语法：
[CONSTRAINT symbol] FOREIGN KEY [id] (index_col_name, ...)
REFERENCES tbl_name (index_col_name, ...)
[ON DELETE {RESTRICT | CASCADE | SET NULL | NO ACTION}]
[ON UPDATE {RESTRICT | CASCADE | SET NULL | NO ACTION}]

2.创建外键
建立表时直接建立外键关联，注意本表的外键列类型与指定的主表列相同，且主表指定列需为主键
CREATE TABLE `person` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` tinyint DEFAULT 0,
  `sex` enum('m','w','o') DEFAULT 'o',
  `salary` decimal(10,2) DEFAULT 250.00,
  `hire_date` date NOT NULL,
  `dept_id` int DEFAULT NULL,
   constraint dept_fk foreign key(dept_id) references dept(id));
   建立表后增加外键
    alter table person add constraint dept_fk foreign key(dept_id) references dept(id);
    
    ３．通过外键名称解除外键约束
    alter table person drop foreign key dept_fk;
删除外键后发现desc查看索引标志还在，其实外键也是一种索引，需要将外键名称的索引删除之后才可以。

４．级联选项
- restrict(默认)  :  on delete restrict  on update restrict
    - 当主表删除记录时，如果从表中有相关联记录则不允许主表删除
    - 当主表更改主键字段值时，如果从表有相关记录则不允许更改
- cascade ：数据级联更新  on delete cascade   on update cascade
    - 当主表删除记录或更改被参照字段的值时,从表会级联更新
- set null  :   on delete set null    on update set null
    - 当主表删除记录时，从表外键字段值变为null
    - 当主表更改主键字段值时，从表外键字段值变为null
- no action
    - 同 restrict，都是立即检查外键限制
```

8.表关联设计

```mysql
1.一对一关系
一张表的一条记录一定只能与另外一张表的一条记录进行对应，反之亦然。
举例 :  学生信息和学籍档案，一个学生对应一个档案，一个档案也只属于一个学生
create table student(id int primary key auto_increment,name varchar(50) not null);

create table record(id int primary key auto_increment,
comment text not null,
st_id int unique,
foreign key(st_id) references student(id) 
on delete cascade 
on update cascade
);

2.一对多关系
一张表中有一条记录可以对应另外一张表中的多条记录；但是反过来，另外一张表的一条记录
只能对应第一张表的一条记录，这种关系就是一对多或多对一

举例： 一个人可以拥有多辆汽车，每辆车登记的车主只有一人。
create table person(
  id varchar(32) primary key,
  name varchar(30),
  sex char(1),
  age int
);

create table car(
  id varchar(32) primary key,
  name varchar(30),
  price decimal(10,2),
  pid varchar(32),
  constraint car_fk foreign key(pid) references person(id)
);

3.- 多对多关系（需要创建第三张表）
> 一对表中（A）的一条记录能够对应另外一张表（B）中的多条记录；同时B表中的一条记录
> 也能对应A表中的多条记录
>
> 举例：一个运动员可以报多个项目，每个项目也会有多个运动员参加,这时为了表达多对多关系需要单独创建关系表。
CREATE TABLE `athlete` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `age` tinyint NOT NULL,
  `country` varchar(30) NOT NULL,
  `description` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rname` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `athlete_item` (
  `aid` int NOT NULL,
  `tid` int NOT NULL,
  PRIMARY KEY (`aid`,`tid`),
  CONSTRAINT `athlete_fk` FOREIGN KEY (`aid`) REFERENCES `athlete` (`id`),
  CONSTRAINT `item_fk` FOREIGN KEY (`tid`) REFERENCES `item` (`id`)
);
```

9.E-R模型

```mysql
1.定义
E-R模型(Entry-Relationship)即 实体-关系 数据模型,用于数据库设计
用简单的图(E-R图)反映了现实世界中存在的事物或数据以及他们之间的关系

2.实体
1、描述客观事物的概念
2、表示方法 ：矩形框
3、示例 ：一个人、一本书、一杯咖啡、一个学生

3.属性
1、实体具有的某种特性
2、表示方法 ：椭圆形
3、示例
   学生属性 ：学号、姓名、年龄、性别、专业 ... 
   感受属性 ：悲伤、喜悦、刺激、愤怒 ...
   
   4.关系
   1、实体之间的联系
2、一对一关联(1:1)
3、一对多关联(1:n)
4、多对多关联(m:n) 

5.ER图的绘制

矩形框代表实体,菱形框代表关系,椭圆形代表属性
```

10.表关联查询

```mysql
1.多表查询
多个表数据可以联合查询，语法格式如下：
select  字段1,字段2... from 表1,表2... [where 条件]
e.g.
select * from dept,person where dept.id = person.dept_id;

2.内连接
内连接查询只会查找到符合条件的记录，其实结果和表关联查询是一样的,官方更推荐使用内连接查询。
SELECT 字段列表
    FROM 表1  INNER JOIN  表2
ON 表1.字段 = 表2.字段;
select * from person inner join  dept  on  person.dept_id =dept.id;

2.外链接
左连接  : 左表为主表，显示右表中与左表匹配的项
SELECT 字段列表
    FROM 表1  LEFT JOIN  表2
ON 表1.字段 = 表2.字段;
select * from person left join  dept  on  person.dept_id =dept.id;

右连接 ：右表为主表，显示左表中与左表匹配的项
SELECT 字段列表
    FROM 表1  RIGHT JOIN  表2
ON 表1.字段 = 表2.字段;
select * from person right join  dept  on  person.dept_id =dept.id;

注意：我们尽量使用数据量大的表作为基准表，即左连接做左表，右连接做右表

```

11.视图

```sql
1.概念
视图是存储的查询语句,当调用的时候,产生结果集,视图充当的是虚拟表的角色。其实视图可以理解为一个表或多个表中导出来的表，作用和真实表一样，包含一系列带有行和列的数据 视图中，用户可以使用SELECT语句查询数据，也可以使用INSERT，UPDATE，DELETE修改记录，视图可以使用户操作方便，并保障数据库系统安全，如果原表改名或者删除则视图也失效。

2.创建视图
语法结构：
CREATE [OR REPLACE] VIEW [view_name] AS [SELECT_STATEMENT];
释义：
CREATE VIEW： 创建视图
OR REPLACE : 可选，如果添加原来有同名视图的情况下会覆盖掉原有视图
view_name ： 视图名称
SELECT_STATEMENT ：SELECT语句
e.g.
create view  c1 as select name,age from class_1;

3.视图表的增删改查操作
视图的增删改查操作与一般表的操作相同，使用insert update delete select即可，但是原数据表的约束条件仍然对视图产生作用。

4.删除视图
drop view [IF EXISTS] 视图名；
IF EXISTS 表示如果存在，这样即使没有指定视图也不会报错。
drop view c1;

5.修改视图
参考创建视图，将create关键字改为alter
alter view  c1 as select name,age,score from class_1;

6.视图作用
- 作用
    1. 是对数据的一种重构，不影响原数据表的使用。
    2. 简化高频复杂操作的过程，就像一种对复杂操作的封装。
    3. 提高安全性，可以给不同用户提供不同的视图
    4. 让数据更加清晰
- 缺点
    1. 视图的性能相对较差，从数据库视图查询数据可能会很慢
    2. 表依赖关系处理麻烦，根据数据库的基础表创建一个视图。每当更改视图或者原表时，另一个也会修改。
```

12.函数和存储过程

```sql
1.概念
存储过程和函数是事先经过编译并存储在数据库中的一段sql语句集合，调用存储过程和函数可以简化应用开发工作，提高数据处理的效率

2.创建函数
delimiter 自定义符号　　-- 如果函数体只有一条语句, begin和end可以省略, 同时delimiter也可以省略
　　create function 函数名(形参列表) returns 返回类型　　-- 注意是retruns
　　begin
　　　　函数体　　　　-- 函数语句集,set @a 定义变量
　　　　return val
　　end  自定义符号
delimiter ;
e.g. 含有参数的函数调用
delimiter $$
create function queryNameById(uid int(10)) 
returns varchar(20)
begin
return  (select name from class_1 where id=uid);
end $$
delimiter ;

select queryNameById(1);

3.存储过程创建
创建存储过程语法与创建函数基本相同，但是没有返回值。
delimiter 自定义符号　
　　create procedure 存储过程名(形参列表)
　　begin
　　　　存储过程　　　　-- 存储过程语句集,set @a 定义变量
　　end  自定义符号
delimiter ;
e.g. 存储过程创建和调用
delimiter $$
create procedure st() 
begin 
    select name,age from class_1; 
    select name,score from class_1 order by score desc; 
end $$
delimiter ;

call st();

存储过程三个参数的区别
- IN 类型参数可以接收变量也可以接收常量，传入的参数在存储过程内部使用即可，但是在存储过程内部的修改无法传递到外部。
- OUT 类型参数只能接收一个变量，接收的变量不能够在存储过程内部使用（内部为NULL），但是可以在存储过程内对这个变量进行修改。因为定义的变量是全局的，所以外部可以获取这个修改后的值。
- INOUT类型参数同样只能接收一个变量，但是这个变量可以在存储过程内部使用。在存储过程内部的修改也会传递到外部。
- 设置变量方法：   set  @[变量名] = 值； 表示这是一个用户变量，使用时用@[变量名]。 在函数内部设置declare [变量名] [变量类型]为局部变量，局部变量可以使用set赋值或者着使用into关键字。
e.g. : 分别将参数类型改为IN OUT INOUT 看一下结果区别
delimiter $$
create procedure p_out ( OUT num int )
begin
    select num;
    set num=100;
    select num;
end $$
delimiter ;
set @num=10;
call p_out(@num)

4.调用存储过程
call 存储过程名字（[存储过程的参数[,……]])

5.调用存储函数
select 存储函数名字（[存储过程的参数[,……]])

6.使用show status语句查看存储过程和函数的信息
show {procedure|function} status [like’存储过程或存储函数的名称’]

7.使用show create语句查看存储过程和函数的定义
show create  {procedure|function}  存储过程或存储函数的名称

8.删除存储过程或存储函数
DROP {PROCEDURE | FUNCTION} [IF EXISTS] sp_name

9.函数和存储过程区别
        1. 函数有且只有一个返回值，而存储过程不能有返回值。
        2. 函数只能有输入参数，而存储过程可以有in,out,inout多个类型参数。
        3. 存储过程中的语句功能更丰富，实现更复杂的业务逻辑，可以理解为一个按照预定步骤调用的执行过程，而函数中不能展示查询结果集语句，只是完成查询的工作后返回一个结果，功能针对性比较强。
        4. 存储过程一般是作为一个独立的部分来执行(call调用)。而函数可以作为查询语句的一个部分来调用。
```



13.事务控制
MySQL 事务主要用于处理操作量大，复杂度高的数据。比如说，在人员管理系统中，你删除一个人员，既需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等，如果操作就必须同时操作成功，如果有一个不成功则所有数据都不动。这时候数据库操作语句就构成一个事务。事务主要处理数据的增删改操作。
作用：
确保数据操作过程中的一致性、完整性、准确性、有效性

```mysql
1.事务四大特性  （需要背诵）
            1. 原子性（atomicity）
            > 一个事务必须视为一个不可分割的最小工作单元，对于一个事务来说，不可能只执行其中的一部分操作,整个事务中的所有操作要么全部提交成功，要么全部失败回滚
            2. 一致性（consistency）
            > 事务完成时，数据必须处于一致状态，数据的完整性约束没有被破坏。
            3. 隔离性（isolation）
            > 数据库允许多个并发事务同时对其数据进行读写和修改的能力，而多个事务相互独立。隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。
            4. 持久性（durability）
            > 一旦事务提交，则其所做的修改就会永久保存到数据库中。此时即使系统崩溃，修改的数据也不会丢失。

2.开启事务
   mysql>begin; # 方法1
   mysql>start transaction; # 方法2
   开始执行事务中的若干条SQL命令（增删改）
	 终止事务，若begin之后使用commit提交事务，使用rollback进行事务回滚。
  mysql>commit; # 事务中SQL命令都执行成功,提交到数据库,结束!
   mysql>rollback; # 有SQL命令执行失败,回滚到初始状态,结束!

3.事务隔离级别
事务四大特性中的隔离性是在使用事务时最为需要注意的特性，因为隔离级别不同带来的操作现象也有区别
隔离级别
- 读未提交：read uncommitted
    > 事物A和事物B，事物A未提交的数据，事物B可以读取到
    > 这里读取到的数据叫做“脏数据”
    > 这种隔离级别最低，这种级别一般是在理论上存在，数据库隔离级别一般都高于该级别
- 读已提交：read committed
    > 事物A和事物B，事物A提交的数据，事物B才能读取到
    > 这种隔离级别高于读未提交
    > 换句话说，对方事物提交之后的数据，我当前事物才能读取到
    > 这种级别可以避免“脏数据”
    > 这种隔离级别会导致“不可重复读取”
- 可重复读：repeatable read
    > 事务A和事务B，事务A提交之后的数据，事务B读取不到
    > 事务B是可重复读取数据
    > 这种隔离级别高于读已提交
    > MySQL默认级别
    > 虽然可以达到可重复读取，但是会导致“幻像读”
- 串行化：serializable
    > 事务A和事务B，事务A在操作数据库时，事务B只能排队等待
    > 这种隔离级别很少使用，吞吐量太低，用户体验差
    > 这种级别可以避免“幻像读”，每一次读取的都是数据库中真实存在数据，事务A与事务B串行，而不并发

```



14.数据库优化

```
数据库设计范式
- 第一范式： 数据库表的每一列都是不可分割的原子数据项，而不能是集合，数组，记录等组合的数据项。简单来说要求数据库中的表示二维表，每个数据元素不可再分。

    例如： 在国内的话通常理解都是姓名是一个不可再拆分的单位，这时候就符合第一范式；但是在国外的话还要分为FIRST NAME和LAST NAME，这时候姓名这个字段就是还可以拆分为更小的单位的字段，就不符合第一范式了。

- 第二范式： 第二范式（2NF）要求数据库表中的每个实例或记录必须可以被唯一地区分，所有属性依赖于主属性。即选取一个能区分每个实体的属性或属性组，作为实体的唯一标识，每个属性都能被主属性筛选。其实简单理解要设置一个区分各个记录的主键就好了。

- 第三范式： 在第二范式的基础上属性不传递依赖，即每个属性于其它非主属性。要求一个关系中不包含已在其它关系已包含的非主关键字信息。其实简单来说就是合理使用外键，使不同的表中不要有重复的字段就好了
```





15.MySQL存储引擎

```mysql
mysql数据库管理系统中用来处理表的处理器

1.基本操作
            1、查看所有存储引擎
               mysql> show engines;
            2、查看已有表的存储引擎
               mysql> show create table 表名;
            3、创建表指定
               create table 表名(...)engine=MyISAM,charset=utf8,auto_increment=10000;
            4、已有表指定
               alter table 表名 engine=InnoDB;
               
2.InnoDB		
        1、支持行级锁,仅对指定的记录进行加锁，这样其它进程还是可以对同一个表中的其它记录进行操作。
        2、支持外键、事务、事务回滚
        3、表字段和索引同存储在一个文件中
           1、表名.frm ：表结构
           2、表名.ibd : 表记录及索引文件
           
3. MyISAM
            1、支持表级锁,在锁定期间，其它进程无法对该表进行写操作。如果你是写锁，则其它进程则读也不允许
            2、表字段和索引分开存储
               1、表名.frm ：表结构
               2、表名.MYI : 索引文件(my index)
               3、表名.MYD : 表记录(my data)

4.如何选择存储引擎
            1、执行查操作多的表用 MyISAM(使用InnoDB浪费资源)
            2、执行写操作多的表用 InnoDB
            CREATE TABLE tb_stu(
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `name` varchar(30) DEFAULT NULL,
            `sex` varchar(2) DEFAULT NULL,
            PRIMARY KEY (`id`)
            )ENGINE=MyISAM DEFAULT CHARSET=utf8;
            
            
5. explain语句
        使用 EXPLAIN 关键字可以模拟优化器执行SQL查询语句，从而知道MySQL是如何处理你的SQL语句的。这可以帮你分析你的查询语句或是表结构的性能瓶颈。通过explain命令可以得到:
        - 表的读取顺序
        - 数据读取操作的操作类型
        - 哪些索引可以使用
        - 哪些索引被实际使用
        - 表之间的引用
        - 每张表有多少行被优化器查询     

```



16.SQL优化

```sql
- 尽量选择数据类型占空间少，在where ，group by，order by中出现的频率高的字段建立索引
- 尽量避免使用 select * ...;用具体字段代替 * ,不要返回用不到的任何字段 
- 少使用like %查询，否则会全表扫描
- 子查询优化为join查询
- 控制使用自定义函数
- 单条查询最后添加 LIMIT 1，停止全表扫描
- where子句中不使用 != ,否则放弃索引全表扫描
- 尽量避免 NULL 值判断,否则放弃索引全表扫描
    优化前：select number from t1 where number is null;
    优化后：select number from t1 where number=0;
    - 在number列上设置默认值0,确保number列无NULL值
- 尽量避免 or 连接条件,否则会放弃索引进行全表扫描，可以用union代替
    优化前：select id from t1 where id=10 or id=20;
    优化后： select id from t1 where id=10 union all 
            select id from t1 where id=20;
- 尽量避免使用 in 和 not in,否则会全表扫描
    优化前：select id from t1 where id in(1,2,3,4);
    优化后：select id from t1 where id between 1 and 4;
```



17.数据库备份和用户管理

```sql
1.表的复制
        1、表能根据实际需求复制数据
        2、复制表时不会把KEY属性复制过来
        create table 表名 select 查询命令;
        
2. 数据备份
        1. 备份命令格式
        > mysqldump -u用户名 -p 源库名 > ~/stu.sql
        >
        > > --all-databases  备份所有库
        > > db_name            备份单个库
        > > -B 库1 库2 库3   备份多个库
        > > 库名 表1 表2 表3 备份指定库的多张表
        
        2. 恢复命令格式
		> mysql -uroot -p 目标库名 < stu.sql
		
3.		用户权限管理
            开启MySQL远程连接
            更改配置文件，重启服务！
            1.sudo  su
            2.cd /etc/mysql/mysql.conf.d
            3.cp mysqld.cnf mysqld.cnf.bak
            4.vi mysqld.cnf #找到44行左右,加 # 注释
               #bind-address = 127.0.0.1
               [mysqld]
               character_set_server = utf8
            5.保存退出
            6.service mysql restart
            7.修改用户表host值 
              use mysql;
              update user set host='%' where user='root';
            8.刷新权限
              flush privileges;
              
4.添加授权用户
            1. 用root用户登录mysql
               mysql -uroot -p123456
            2. 添加用户 % 表示自动选择可用IP
               CREATE USER 'username'@'host' IDENTIFIED BY 'password';
            3. 授权
               grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
            4. 刷新权限
               flush privileges;
            权限列表
            all privileges 、select 、insert ，update，delete，alter等。
        库.表 ： *.* 代表所有库的所有表
               
5.示例
        1. 创建用户
          mysql>create user  'work'@'%'  identified by '123';
        2. 添加授权用户work,密码123,对所有库的所有表有所有权限
          mysql>grant all privileges on *.* to 'work'@'%' identified by '123' with grant option;
          mysql>flush privileges;
        3. 添加用户duty，密码123,对db2库中所有表有所有权限
          mysql>grant all privileges on books.* to 'duty'@'%' identified by '123' with grant option;
          mysql>flush privileges;
```



18.pymysql模块

```python
1. pymysql安装
> sudo pip3 install pymysql

2.pymysql使用流程
                1. 建立数据库连接(db = pymysql.connect(...))
                2. 创建游标对象(cur = db.cursor())
                3. 游标方法: cur.execute("insert ....")
                4. 提交到数据库或者获取数据 : db.commit()/db.fetchall()
                5. 关闭游标对象 ：cur.close()
                6. 断开数据库连接 ：db.close()
                
3. 解释
            db = pymysql.connect(参数列表)
                            > host ：主机地址,本地 localhost
                            > port ：端口号,默认3306
                            > user ：用户名
                            > password ：密码
                            > database ：库
                            > charset ：编码方式,推荐使用 utf8
                            
              数据库连接对象(db)的方法
                            > cur = db.cursor() 返回游标对象,用于执行具体SQL命令
                            > db.commit() 提交到数据库执行
                            > db.rollback() 回滚，用于当commit()出错是回复到原来的数据形态
                            > db.close() 关闭连接              
                          
                        
				游标对象(cur)的方法
                            > cur.execute(sql命令,[列表]) 执行SQL命令
                            > cur.executemany(sql命令,[data]) 根据数据列表项多次执行SQL命令，一般用于写操作。
                            > cur.fetchone() 获取查询结果集的第一条数据，查找到返回一个元组否则返回None
                            > cur.fetchmany(n) 获取前n条查找到的记录，返回结果为元组嵌套元组， ((记录1),(记录2))。
                            > cur.fetchall() 获取所有查找到的记录，返回结果形式同上。
                            > cur.close() 关闭游标对象                       
```







































