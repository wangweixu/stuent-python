#coding:utf-8


##=====异常处理=====##
try:
    f = file('non.txt')
    print 'File opened'
    f.close()                #若能打开non.txt，则输出打印“Flie opened”；
except:
    print 'File not exists'  #若不能打开non.txt，则输出打印“File not exists”
print 'Bone'                 #无论结果如何，整个程序不会中断，最后都会输出“Done”
