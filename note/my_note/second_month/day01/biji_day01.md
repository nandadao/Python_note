## day01吕泽



## 1.什么是后端

​		操作系统：

​		前端/前台/客户端

​				功能：收集用户请求、发送请求、得到服务器数据、展示数据

​		后端/后台/服务端

​				环境：服务器主机（Linux）

​				功能：处理请求，将结果数据提供给前端

​				安全保证：

​				并发保证：

​				更快的算法方法



## 2. Linux操作系统简介

  1. Linux操作系统的结构

       1. cookie: 

            1. Linux文件： b (块设备驱动文件)     	

               ​						 c (字符设备文件)          

               ​						 **d (目录/文件夹)**

               ​					     **- (普通文件)**   

               ​						 l (链接文件)

                 						s (套接子文件) 

               ​						  p (管道文件)

             		2.  bin :二进制可执行文件
	
             		3. etc
	
             		4. home
	
             		5. usr

2. 绝对路径和相对路径

3. 环境变量

    查看环境变量 echo $PATH

    1. 在python文件中添加      #!/usr/bin/env python3
    2. 使用  chmod  777  hello.py  修改可执行权限
    3. 将文件移动到    /bin  下，  sudo   cp  hello.py    /bin

4. Linux基础命令

    1. **sudo   su** 进入root 权限，推出exit

    2. shutdown   +5:表示五分钟后关闭电脑

    3. **man**：用法  man  ls:查看ls的帮助：有问题找man（男人）

    4. CTRL + ALT + T:开启一个新终端         Ctrl +  +放大

        Ctrl  + N  :打开一个新终端

        Ctrl  + Shift + T  :打开一个新窗口

    5. ​     1T   =  1024GB         1G = 1024M        1m=1024K      1k = 1024 bytes(字节)     1bytes  = 8 bit

        一个英文字母占一个字节

    6.    **ls**  -l    >  file.txt :把本来应该打印在终端的写入file.txt中，

        ​	两个>，表示追加

        wc     >  file.txt    ：  6  31 179

    7. rmdir只能删除空目录

    8. **cp**   -r  :写了-r  才可以复制目录

          cp -r .    /home/tarena/   ：复制当前目录到主目录

    9. find         :

    10. file  : 查看文件信息

    11. diff file file1：查看两个文件的不同之处

    12. **wc**   test.py :  wc -l  test.py :查看多少行

        wc -w  test.py :查看多少单词

        wc -c  test.py   查看多少字节

    13. grep:查找文件中的内容，把找到的内容标红色

        ls   |   grep    "file"  :

        file
        file1
        file2
        file3

    14.  ls | wc -w ：5    ：查看当前文件的个数

    15. Ln :创建链接

        ln    -s  :软链接， 删除原文件，链接不能用

    16. date:显示当前时间

    17. df  :显示磁盘信息

        df -Th ：

    18. which  ：查看一个程序的位置



=======================================

作业：

进制转换自学

1. markdown:自己查阅，熟练使用

2. 常用shell命令熟练

3. 进制转换/split()    join()     format()     strip()    :查看字符串的几个方法

4. import    time

    ctime()

    sleep():查阅这两个time模块的方法使用

======================================================================

答案：

​	3.

1. Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。

   **注意：**该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

```pytho
str.strip([chars]);
```

2. join(seq)
   以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

[

3. split(str="", num=string.count(str))
   num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串

4. Python2.6 开始，新增了一种格式化字符串的函数 **str.format()**，它增强了字符串格式化的功能。

   基本语法是通过 **{}** 和 **:** 来代替以前的 **%** 。

   format 函数可以接受不限个参数，位置可以不按顺序。

   ## 实例

```python
>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
 
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
 
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
```

5. # Python time ctime()方法

   ------

   ## 描述

   Python time ctime() 函数把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。 如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于 asctime(localtime(secs))。

   ## 语法

   ctime()方法语法：

   ```python
   time.ctime([ sec ])
   ```

   ## 参数

   - sec -- 要转换为字符串时间的秒数。

   ## 返回值

   该函数没有任何返回值。

   ## 实例

   以下实例展示了 ctime() 函数的使用方法：

   ```python
   #!/usr/bin/python
   import time
   
   print "time.ctime() : %s" % time.ctime()
   ```

   以上实例输出结果为：

   ```python
   time.ctime() : Tue Feb 17 10:00:18 2013
   ```





6. # Python time sleep()方法

   ------

   ## 描述

   Python time sleep() 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。

   ## 语法

   sleep()方法语法：

   ```python
   time.sleep(t)
   ```

   ## 参数

   - t -- 推迟执行的秒数。

   ## 返回值

   该函数没有返回值。

   ## 实例

   以下实例展示了 sleep() 函数的使用方法：

   ## 实例

   \#!/usr/bin/python import time   print "Start : %s" % time.ctime() time.sleep( 5 ) print "End : %s" % time.ctime()

   以上实例输出结果为：

   ```python
   Start : Tue Feb 17 10:19:18 2013
   End : Tue Feb 17 10:19:23 2013
   ```

























































​				

