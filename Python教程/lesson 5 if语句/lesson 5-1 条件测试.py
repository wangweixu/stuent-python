# coding:utf-8

print('---使用and检查多个条件---')
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # and 是多个条件同时满足
print(age_0 >= 21 and age_1 <= 21)

print('\n---使用or检查多个条件---')
age_2 = 22
age_3 = 18
print(age_2 >= 21 or age_3 >= 21)
print(age_2 <= 21 and age_3 >= 21)

print('\n---in检查特定值是否在列表中---')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # mushrooms是否在requested_toppings中
print('pepperoni' in requested_toppings)

print('\n---"not in"检查特定值是否在列表中---')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' not in requested_toppings)  # mushrooms是否不在requested_toppings中
print('pepperoni' not in requested_toppings)
