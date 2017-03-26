print "please enter the value of x"
x = input()
#print "please enter the value of y"
y = input()
#print x,y

from random import randint
a = randint(1,x)
b = randint(1,y)
#print a,b
c = False
d = a

if a >= b:
   print "False,because a>=b"
   print a,b

if a < b:
   while c == False:
         a += 1
         d += a
         #print a
         #print d
         if a >= (b-1):
            c = True
            #print c
            print d
