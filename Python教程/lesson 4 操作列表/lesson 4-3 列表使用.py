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

print('\n---复制列表，将一个列表复制到另外一个列表---')
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\n My friend's favorite foods are:")
print(friend_foods)

print('\n---复制列表，指向同一个列表---')
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')

friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\n My friend's favorite foods are:")
print(friend_foods)