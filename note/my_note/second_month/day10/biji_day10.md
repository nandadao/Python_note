## 复习

１．网络并发模型

　充分利用多个线程进程之间，互不干扰

fork_server　　process_server　　thread_server

２．文件服务（结构，分发思想，请求确认机制）





３．IO模型

　重点讲：阻塞IO　　非阻塞IO　　IO多路复用

> 阻塞IO：不满足执行条件时，或者IO操作时，耗时较长，
>
> 　　　　特点：IO的默认形态，效率低，实现简单
>
> 非阻塞IO：将原本的阻塞函数变为非阻塞
>
> 　　　　函数：setblocking()　　settimeout()　是socket的两个是属性函数
>
> IO多路复用：

## 新知识

### １．IO多路复用

１．定义

２．具体方案

```python
select方法:　windows  linux  unix
poll方法:  linux  unix
epoll方法:  linux　　（执行效率相对较高）
```

### ２．select方法

１．rs, ws, xs = select(rlist, wlist, xlist[, timeout] )　　其中　rlist　用的最多，xlist　基本不用

> 功能：监控IO事件，阻塞等待IO发生
>
> 参数

**注意：两端有尖括号的是对象**

<_io.TextIOWrapper name='file' mode='r' encoding='UTF-8'>

### ３．位运算

１．定义：将整数转换为二进制，按二进制进行运算

２．运算符号：第二阶段只用　　与和或

> &：按位与
>
> | ：或
>
> ^：异或

进制转换：

```
1 -> 1
2 -> 10
4 -> 100
8 -> 1000
16 -> 10000
```

### ４．poll方法

```python
p = select.poll()  # 创建poll对象

p.register(fd, event)  # 注册关注的IO事件
					fd:要关注的IO
        			event:要关注的IO事件类型
　　　　　e.g.      p.register(sockfd, POLLIN | POLLERR)
    
p.unregister(fd)  ：fd可以填IO对象和文件描述符fileno
　　　　　返回值： [(fileno, event) ,   (), ......]  
    				　　　　　fileno文件描述符
        								 event:就绪IO的事件类型
```

### ５．epoll

### ６．三个方法特征对比

**IO多路复用**

```
select  ：
跨平台最好  windows  linux  unic　　
效率一般　
最多监控  1024  个IO
```

```
poll：
跨平台一般　unix   linux　　　
效率一般
监控IO没有限制（可以监测几万个）
```

```
epoll：
跨平台差 linux
效率高
监控IO没有限制

高效率：
				１．不必每次监控向系统层映射IO对象
				２．在应用层可以直接操作就绪IO减少了IO遍历
```

平时最常用的是  select   和　epoll

**epoll高效率的原因：**
				１．不必每次监控向系统层映射IO对象
				２．在应用层可以直接操作就绪IO减少了IO遍历

epoll支持边缘触发：EPOLLET









































