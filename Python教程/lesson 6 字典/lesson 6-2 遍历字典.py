# coding:utf-8

print("---遍历所有的键-值对---")
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print('\nkey: ' + key)
    print('Value: ' + value)

print('-------')
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language is " + languages.title())

print("\n---遍历字典中的所有键---")
for name in favorite_languages.keys():
    print(name.title())

print("\n---按顺序遍历字典中的所有键,使用sorted()---")
for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")

print("\n---遍历字典中的所有值---")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n---使用set()删除重复元素---")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
