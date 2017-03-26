#coding:utf-8
from random import randint

f = open('E:\gamefile\game.txt')   #打开game.txt文件
score = f.read().split()           #读取文件中的所有内容，并将其按空格分隔组成list
f.close()
#变量赋值
game_times = int(score[0])      #总游戏次数
min_times = int(score[1])       #最快猜出的轮数
total_times = int(score[2])      #猜过的总轮数

if game_times >0:
    avg_times = float(total_times)/game_times  #平均轮数
else:
    avg_times = 0
print '你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案'%(
    game_times,min_times,avg_times)

num = randint(1,100)
times = 0    #记录本次游戏轮数
print 'Guess what I think?'
bingo = False
while bingo == False:
    times +=1   #轮数+1
    answer = input()
    if answer < num:
        print 'too small'
    elif answer >num:
        print 'too big'
    else:
        print 'BINGO!'
        bingo = True
#如果是第一次玩，或者本次的轮数比最小轮数还小，就记录本次成绩为最小轮数
if game_times == 0 or times<min_times:
    min_times = times
total_times += times  #总游戏轮数增加
game_times += 1     #游戏次数加1
result = '%d %d %d'%(game_times,min_times,total_times)
f = open('E:\gamefile\game.txt','w')
f.write(result)
f.close()
