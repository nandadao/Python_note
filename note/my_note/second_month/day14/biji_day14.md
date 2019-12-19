### 复习

１．

５．聚合

×　select 语句执行顺序
×　聚合函数：avg()    max()　min()   sum()   count()
×　分组：group by  [col]
×　聚合筛选：having  后面可以使用聚合函数
×　去重：distinct
×　聚合运算：select   ccol 加减乘除  from 表

６．索引操作

根据原本的数据表设置的一个方便快速查询的新的表
优点：提高查询效率
缺点：占用额外的物理空间，降低写效率

适合创建索引：数据量大，频繁查询而不是修改

分类：primary key ：不能重复，不可以为空
			index ：没有约束（普通索引用的比较多）
			unique：数值不能重复，但是可以为空

查看索引：desc      (key  -->  MUL  UNI   PRI)
					 show index from [tb];
创建索引：１．create  table  [tb]  (col type...,  index   index_name(col));
					  ２．create index   [index_name ]  on tb(col);
删除索引：drop index 	[index_name]	 on [tb];

==============================================================

### 新知识

### １．外键约束和表关联关系

外键缺点：会降低表的查询效率
主表和从表：foreign key外键一定在从表中
外键语法：外键也是索引（是普通索引）

```mysql
[外键名字]　foreign key [id](从表的字段)   (index_col_name, ....)
references tb1_name(这是主表)  (index_col_name, ....)
```

### ２．表关联设计

１．一对一
２．一对多
３．多对多

### ３．关联查询

１．多表查询

```mysql
# 查询两个表中名字相同的同学
select cls.name,interest.hobby,cls.score from cls,interest where cls.name = interest.name;
select c.name,i.hobby,c.score from cls as c,interest as i where c.name = i.name;
```

２．内连接
SELECT 字段列表
FROM 表1 INNER JOIN 表2　　　（通常把数据量大的表放在前面）
ON 表1.字段 = 表2.字段;

```mysql
select person.name,dept.dname from dept inner join person on dept.id = person.dept_id;
select person.name,dept.dname from dept inner join person on dept.id = person.dept_id where person.salary > 15000;
# 可以加where ,做进一步的筛选
```

３．外连接

```mysql
select dept.dname,person.name from dept left join person on dept.id = person.dept_id;
# cls左边，interest 右边，查找人名的对应关系
select c.name,c.score,i.hobby from cls as c left join interest as i on c.name = i.name where c.score > 80;
```



＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

### 作业：

１．对book表进行重组
２．分为　　书籍表　　作者表　和　出版社表

```
１．通过ER模型规划三个表的内容和关系
２．设计三者之间的关系（自己定）
３．根据你的设计创建三个表，完善表关系
```

３．熟悉语句





























