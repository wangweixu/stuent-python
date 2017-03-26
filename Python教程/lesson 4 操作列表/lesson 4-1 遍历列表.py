#coding:utf-8
magicians = ['alice','david','carolina']

print('----遍历整个列表----')
for magician in magicians:     #从magicians列表中取出一个值，并赋值给变量magician。
    print(magician)

print('\n----在for循环中更多的操作----')
for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see you next trick,"+magician.title()+".\n")

print('\n----在for循环结束后执行一些操作---')
for magician in magicians:
    print(magician.title()+",that was a great trick!")
    print("I can't wait to see you next trick,"+magician.title()+".\n")
print("Thank you,everyone.That was a great magic show!")
