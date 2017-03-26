# coding:utf-8

print '============读文件内的所有内容================'
f = file("E:\Python imformation\Python.txt")  #读文件
date = f.read()   #读文件内的所有内容
print date
f.close()  #关闭文件，释放资源

print '============读取文件内的一行内容============='
f = file("E:\Python imformation\wangweixu.txt")  #读文件
date = f.readline()   #读取一行内容
print date
f.close()  #关闭文件，释放资源

print '========把内容按行读取，存至一个list中======='
f = file("E:\Python imformation\wangweixu.txt")  #读文件
date = f.readlines()   #把内容按行读取，存至一个list中
print date
f.close()  #关闭文件，释放资源

print '====写文件，原文件会被写入的内容覆盖=========='
b = 'I will be in a file.\nSo coo;!'
a = open("E:\Python imformation\wangweixu1.txt",'w')  #写文件，原文件会被写入的内容覆盖
a.write(b)
a.close()  #关闭文件，释放资源

print '============将b文件存储到a文件里============='
a = file("E:\Python imformation\wangweixu12.txt",'w') #创建文件
b = file("E:\Python imformation\Python.txt")  #读文件
date = b.read()   #读文件内的所有内容
a.write(date)    #写入内容
a.close()  #关闭文件，释放资源

print '==========在a文件后面写入b内容==============='
a = file("E:\Python imformation\wangweixu12.txt",'a') #在原文件的基础上增加
b = file("E:\Python imformation\wangweixu.txt")  #读文件
date = b.read()   #读文件内的所有内容
a.write(date)    #写入内容
a.close()  #关闭文件，释放资源
