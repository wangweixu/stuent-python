# coding:utf-8
a = 1         # 先a设为1
while a != 0:   # 先a不等于0就一直做
    print "please input"
    a = input()
print "over"

mun = 10
bingo = True

print "Guess what I think?"
while bingo:
    answer = input()
    if answer < mun:
        print "too small!"
    if answer > mun:
        print "too big!"
    if answer == mun:
        print "BINGO!"
        bingo = True
