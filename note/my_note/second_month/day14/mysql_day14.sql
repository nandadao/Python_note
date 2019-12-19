

-- 用户表
create table user (
    id int primary key auto_increment,
    name varchar(20) not null,
    age tinyint not null,
    sex enum("m","w")
);

-- 朋友圈
create table pyq (
    id int primary key auto_increment,
    content text,
    address varchar(64),
    time datetime,
    image char(100),
    user_id int,
    constraint user_fk foreign key(user_id) references user(id)
);

# 点赞
create table dz_pl (id int primary key auto_increment,
                    user_id int,
                    pyq_id int,
                    dz char,
                    comment text,
                    constraint user_fk1 foreign key(user_id) references user(id),
                    constraint pyq_fk foreign key(pyq_id) references pyq(id)
                    );



# =========================================================
# 学生课程老师　表关系

# 学生表
create table student1 (id int primary key auto_increment,
                      name varchar(32),
                      age tinyint,
                      sex enum("w","m"),
                      address text
);


# 教师
create table teacher (
    id int primary key auto_increment,
    name varchar(32),
    age tinyint,
    title char(12)
);


# 课程表
create table course (
    id int primary key auto_increment,
    c_name varchar(20),
    xf float,
    teacher_id int,
    constraint teacher_fk foreign key course(teacher_id) references teacher(id))
    ;


create table student_course(
    id int primary key auto_increment,
    student_id int,
    course_id int,
    score float,
    constraint student_fk foreign key student_course(student_id) references student1(id),


);






















