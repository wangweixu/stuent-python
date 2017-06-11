# coding: utf-8

print('---将列表存储到字典中1---')
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print('---将列表存储到字典中2---')
favorite_languages = {
    'jen': ['python', 'ruly'],
    'sarah': ['c'],
    'edward': ['ruly', 'go'],
    'phil': ['python', 'haskell'],
}
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language)