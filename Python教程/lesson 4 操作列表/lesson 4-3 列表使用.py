#coding:utf-8

print('----函数range()的使用----')
for value in range(1,5):
    print(value)

print('\n---切片，取前3个元素---')
players = ['charles','martina','michael','florence','eli']
print(players[0:3])

print('\n---遍历切片---')
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for players in players[:3]:
    print(players.title())

