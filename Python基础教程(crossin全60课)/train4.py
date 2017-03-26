# coding:utf-8

from random import choice

score = [0,0]
direction = ['left','center','right']

def kick():
    print '===You Kick!==='
    print 'Choose one side to shoot:'
    print 'left,center,right'
    you = raw_input()       #输入射门角度
    print 'You kicked '+you
    com = choice(direction) #电脑随机扑救方向
    print 'Computer saved '+com
    if you!= com:       #方向不同，进球
        print 'Goal!'
        score[0]+=1   #玩家得分
    else:
        print 'Oops...'
    print 'Score:%d(you)-%d(com)\n'%(score[0],score[1])


    print '===You Save!==='
    print 'Choose one side to save:'
    print 'left,center,right'
    you = raw_input()  #输入补救方向
    print 'You saved '+you
    com = choice(direction)  #电脑随机进球方向
    print 'Computer kicked '+com
    if you == com:   #方向相同，球被扑出
        print 'Saved!'
    else:
        print 'Oops...'
        score[1]+=1  #电脑等分
    print 'Score:%d(you)-%d(com)\n'%(score[0],score[1])

for i in range(1):
    print '====Round %d ===='%(i+1)
    kick()

while(score[0]==score[1]):
    i+=1
    print '====Round %d ===='%(i+1)
    kick()

if score[0]>score[1]:
    print 'You Win!'
else:
    print'You Lose.'
