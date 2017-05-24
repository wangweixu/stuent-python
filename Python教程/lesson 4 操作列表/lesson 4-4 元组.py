# coding:utf-8

print('---元组定义---')
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print('\n---遍历元组中的所有值---')
for dimension in dimensions:
    print(dimension)

print('\n---修改元组变量，将新的元组赋值给变量---')
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
