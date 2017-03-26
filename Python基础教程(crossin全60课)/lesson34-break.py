# coding:utf-8

#如果在循环条件任然满足或序列没有遍历完的时候，想要强行跳出循环，就需要用到break语句。

##========while=========##
#=====while 循环 在条件不满足时 结束=====#
while True:
    a = raw_input()
    if a == 'BOF':
        break

##========for=========##
#=====for 循环 遍历完序列后 结束=====#
for i in range(1,10):
    a = raw_input()
    if a == 'BOF':
        break    
