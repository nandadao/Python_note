"""
	作业：
​	1.写程序，实现对一个文件进行拷贝
​			1.通过input()输入一个文件位置
​			2.将该文件用写的程序拷贝到主目录下，
​			3.文件可能是文本文件，也可能是二进制文件（b）
​			4.文件可能比较大，不允许一次性拷贝完
​	温馨提示：从源文件读取内容，写入到目标新文件（边读，边写）
​	2.字符串函数，进制转换
"""
# ====================老师答案
home = "/home/tarena/"
img = input(">>")
# 打开源文件
fr = open(img, "rb")

filename = img.split("/")[-1]

# 打开新的文件
fw = open(home+filename, "wb")

# 边读边写
while True:
	data = fr.read(1024)
	fw.write(data)
	if not data:
		break

fr.close()
fw.close()










# =================================

# address = input("请输入文件地址：")
#
# f1 = open(address, "rb")
# f2 = open("/home/tarena/file.jpeg", "ab")
#
#

# while True:
# 	data1 = f1.read(1024)
# 	f2.write(data1)
# 	if not data1:
# 		break


# f1.close()
# f2.close()











