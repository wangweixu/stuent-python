# coding:utf-8
#if,elif,else组成的整体的条件语句中：if是必须有，elif可以有很多个，else可以没有，else有的话，要放在条件语句的最后

def isEqual(num1,num2):
    if num1<num2:
        print 'too small'
        return False;
    elif num1>num2:
        print 'too big'
        return False;
    else:
        print 'bingo'
        return True
    
from random import randint
num = randint(1,100)
print 'Guess what I think?'
bingo = False
while bingo == False:
    answer = input()
    bingo = isEqual(answer,num)
