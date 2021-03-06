#coding:utf-8
from random import randint

name = raw_input(u'请输入你的名字：') #输入玩家名字

f = open('E:\gamefile\game.txt')   #打开game.txt文件
lines = f.readlines()
f.close()
#print lines
scores = {}    #初始化一个空字典
for l in lines:
    s = l.split()   #把每一行的数据拆分成list
    #print s
    scores[s[0]] = s[1:] #将第一项元素作为key，剩下的作为value
print scores
score = scores.get(name)  #查找当前玩家的数据
#print score
if score is None:  #如果没有找到，
    score = [0,0,0]  #初始化数据

#变量赋值
game_times = int(score[0])      #总游戏次数
min_times = int(score[1])       #最快猜出的轮数
total_times = int(score[2])      #猜过的总轮数

if game_times >0:
    avg_times = float(total_times)/game_times  #平均轮数
else:
    avg_times = 0
print "%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案"%(
    name,game_times,min_times,avg_times)

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

#把成绩更新到对应的玩家数据中
#加str转化成字符串，为后面的格式化作准备
scores[name] = [str(game_times),str(min_times),str(total_times)]
print scores
result = ''  #初始化一个空字符串，用来存储数据
for n in scores:
    #把成绩按照“name game_times min_times total_times”格式化
    #结尾要加上\n换行
    line = n + ' '+' '.join(scores[n]) + '\n'
    result += line  #添加到result中
    print result
f = open('E:\gamefile\game.txt','w')
f.write(result)
f.close()
