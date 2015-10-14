# week 2
"""
file operations exercise 1
2015.10.14
---
编程小练习（不计分）

创建一个文件src.txt，文件内容为：

How many seas must a white dove sail
Before she sleeps in the sand

将src.txt的内容复制到文件dest.txt中，并在dest.txt文件头部添加另两行字符串，添加后dest.txt文件中的内容为：

How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
"""
# init
str1 = \
'''
How many seas must a white dove sail
Before she sleeps in the sand
'''
str2 = \
'''
How many roads must a man walk down
Before they call him a man
'''
# create
f = open(r'/Users/minconghuang/Desktop/src.txt', 'w')
f.write(str1)
f.close()
# read
f = open(r'/Users/minconghuang/Desktop/src.txt', 'r')
str1 = f.read()
f.close()
# add
f = open(r'/Users/minconghuang/Desktop/dest.txt', 'a+')
f.seek(0, 0) # reset pointer to 0
f.writelines(str2 + str1)
f.close()
