# coding:utf-8

print("---访问字典中的值---")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])    # 输出键'color'的值

print("\n---字典添加键-值对---")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\n---修改字典中的值---")
alien_0['color'] = 'yellow'
print(alien_0)

print("\n---删除字典中的键值对---")
del alien_0['color']
print(alien_0)

print("\n---先创建空白的字典---")
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

print("\n---由类似对象组成的字典---")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      '.')
