# coding:utf-8
from random import randint   #from 模块名 import 方法名，调用随机数函数
mun = randint(1,100)         #产生一个随机数

print "Guess what I think?"
bingo = False

while bingo == False:
      answer = input()

      if answer<0:
            print "Exit game..."
            break
      
      elif answer<mun:
         print "%d is too small!"%answer
         
      elif answer>mun:
         print "%d is too big!"%answer

      else:
         print "BINGO,%d is the right answer"%answer
         bingo = True
