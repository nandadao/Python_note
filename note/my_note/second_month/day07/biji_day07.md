## 回顾

１．孤儿进程和僵尸进程

僵尸进程处理：ｗait()		二级子进程		signal()

２．群聊聊天室

需求分析  ->   总结预设技术点解决方法　-> 　结构拆分，封装设计	-> 确定通信协议	->  

分模块思考逻辑　->　写代码　->　代码测试　->　优化调整

３．multiprocessing多进程(multi多的意思)

p = Process(target = fun1)　创建进程对象

p.start()　启动进程

p.join()　回收进程

## 新知识

## day07

### １．进程对象属性

p.name　进程名称

p.pid　子进程的PID号

p.is_alive()　查看子进程是否在

p.daemon守护：设置父子进程的退出关系

### ２．自定义进程类

１．继承：可以使用父类的方法属性，子类可以添加新功能，重写(覆盖)父类方法

２．如果重写__init  方法添加自己的属性，可以使用super()加载父类属性

### ３．进程池

```python
from multiprocessing import Pool
pool  =  Pool(processes)  # 创建进程池对象，参数制定进程数量
pool.apply_async(fun1, args = (1, ))  # 将事件加入进程池队列执行
pool.close() # 关闭进程池
pool.join()　# 阻塞，回收进程池中的进程

```

### ４．进程间通信（ＩＰＣ）

１．消息队列

```python
from multiprocessing import Queue
q = Queue(5)  # ５表示最多可以存入的消息数量
q.put(data)  # data要存入的内容
data = q.get()  # data是返回的内容，　先进先出
q.full()
q.empty()
q.qsize()
q.close()  # 关闭队列
```

### ５．线程编程（Thread）

１．线程基本概念



## 作业

１．练习没完成的再看看

２．进程两种方法总结

３．函数和类















































