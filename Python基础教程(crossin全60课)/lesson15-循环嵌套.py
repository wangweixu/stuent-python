# coding:utf-8


print u'竖行打印的5个*'
for i in range(0,5):   #竖行循环5次
    print '*'


print
print u'横行打印的5个*'
for j in range(0,5):
    print '*',


print
print
print u'矩阵输出'
for i in range(0,5):
    for j in range(0,5):
        print '*',
    print


print 
print u'三角形'
for i in range(0,5):
    for j in range(0,i+1):
        print '*',
    print
