# coding:utf-8
print range(1,10)

for i in range(1,10):
    print i

I = range(1,10)
for i in I:
    print i


A = [1,1,2,3,5,8,13]
print A

for a in A:
    print a,
print


B = ['wang',1,2,3,5,8,13]

#list全打印
print("\n-----list全打印---")
print B

for b in B:
    print b,
print

##======打印指定list中的值======##
print("\n-----打印指定list中的值---")
print B[0]    #打印第一个元素
print B[-3]   #打印倒数第三个元素

#==切片操作，开始位置包含在切片内，结束位置不包==##
print("\n-----切片操作---")
print B[1:3]  #打印第二个到第三个元素。
print B[:3]   #从第一个元素开始，到第三个元素。
print B[1:]   #从第二个元素到最后一个元素。
print B[:]    #返回整个列表
print B[1:-1] #从第二个到倒数第二个元素。

#===========增加list===========##
print("\n-----增加操作---")
B.append('Tome')
print B

#===========插入list===========##
print("\n-----插入操作---")
B.insert(1,'abc')
print(B)

##============删除list============##
print("\n-----删除操作---")
del B[1]
print B


##=========字符串分割=========##
print("\n-----字符串分割---")
sentence = 'I am an Englist sentence'
a = sentence.split()    #split()会把字符串按照其中的空格进行分割
                        #分割后的每一段都是一个新的字符串，最终返回这些字符串组成一个 list。
print a

#split()默认是按照空白字符进行分割。
#split()可以按空格、换行符\n，制表位\t进行分割。
print("\n-----split('x')，按x来分割---")
section = 'Hi. I am the one. Bye.'
print section.split('.')  #按‘.’来分割

print 'aaa'.split('a')  #按a来分割


##=========连接list=========##
print("\n-----连接---")
s = ':'
li = ['apple','pear','orange']
fruit =s.join(li)
print fruit

#字符串的连接采用.join()
print ':'.join(['A','B','C'])
print ' '.join(['a','b','c'])


##=========字符串的索引和切片=========##
print("\n-----字符串的索引和切片---")
word = 'helloworld'
for c in word:    #遍历：通过for...in可以遍历字符串中的每一个字符
    print c

print word[0]     #索引访问：通过[x]加索引的方式，访问字符串中的第x个字符
print word[-2]


print word[5:7]   #切片：通过两个参数，截取一段子串。
print word[:-5]
print word[:]

print ','.join(word)  #连接字符：可以用join可以对字符串使用，重新连接成新的字符串
print ''.join(word)
