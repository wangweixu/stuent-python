#coding:utf-8

##=====字典======##

print '============查字典里的一个值================'
score = {
    '萧峰':95,
    '段誉':97,
    '虚竹':89
    }
print score['段誉']

print '============遍历的变量中存储的是字典的键================'
for name in score:
    print score[name]   #遍历的变量中存储的是字典的键。

print '============打印变量的key及存储的是字典的键================'
for name in score:
    print name+' '+str(score[name])   

score['虚竹'] = 91      #改变字典中的某一项的值，就直接给这一项赋值
score['慕容复'] = 88    #增加一项字典的方法，给一个新建赋值
del score['萧峰']       #删除一项字典项的方法del

print '============遍历的变量中存储的是字典的键================'
for name in score:
    print name,score[name]

##如果想要新建一个空的字典，只需：  d = {}
