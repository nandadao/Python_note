"""
    练习：利用httpserver程序，编写一个fork多进程程序，让用户既可以通过
​			8000端口访问后端应用，也可以通过8080端口访问后端应用。
在父进程调用一下httpserver程序，
子进程调用一下httpserver程序
"""
import os
from socket import *
from httpserver import *



pid = os.fork()

if pid < 0:
    print("Error")

elif pid == 0:
    # 子进程
    print("Child process")
    # 执行8080
    main(("0.0.0.0", 8000))
else:
    # 父进程
    print("Parent process")
    # 执行8000
    main(("0.0.0.0", 8080))


























