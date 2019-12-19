mysql作业:

```mysql
create database books character set utf8;     :创建数据库

create table book (id int primary key auto_increment,title varchar(32) not null,author varchar(32) not null,price float default 30.0,publication enum("中国教育","机械工业","人民教育"),comment text);

insert into book values (1,"猫","老舍",44.5,"中国教育","好书啊");
insert into book values(2,"三体","刘慈欣",77,"人民教育","不要回答!!!");
insert into book(title,author,price,publication) values("平凡的世界","路遥",66,"机械工业");
insert into book(title,author,price,publication,comment) values("红与黑","司汤达",55.3,"中国教育","没看完");

select * from book where price > 30;

select * from book where publication = "中国教育";

select * from book where author = "老舍" and publication = "中国教育";

select * from book where comment is not null;

select title,price from book where price > 60;



```













