# coding:utf-8

print('----函数range()的使用----')
for value in range(1, 5):
    print(value)

print('\n----使用函数list()将range()的结果直接转换为列表----')
numbers = list(range(1, 5, 2))
print(numbers)

print('\n----列表元素增加----')
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

print('\n----对数字列表进行简单统计----')
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
