# coding: utf-8

print("---字典列表---")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print("\n----自动新增字典列表---")
aliens1 = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens1.append(new_alien)
print(aliens1)

print("\n----使用if-elif来修改字典列表---")
for alien2 in aliens1[0:3]:
    if alien2['color'] == 'green':
        alien2['color'] = 'yellow'
        alien2['speed'] = 'medium'
        alien2['points'] = 10
    elif alien2['color'] == 'yellow':
        alien2['color'] = 'red'
        alien2['speed'] = 'fast'
        alien2['points'] = 15
    print(alien2)
print(aliens1)

