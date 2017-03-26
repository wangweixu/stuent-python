# coding:utf-8
motorcycles = ['honda','yamaha','suzuki']

print("----使用del删除第一元素---")
del_motorcycles = motorcycles[:]   #列表复制
del del_motorcycles[0]
print(del_motorcycles)

print("\n----使用.pop()删除第二个元素，还可以使用该元素的值---")
pop_motorcycles = motorcycles[:]
popped_motorcycles = pop_motorcycles.pop(1)
print(pop_motorcycles)
print(popped_motorcycles)

print("\n----根据值删除元素---")
remove_motorcycles = motorcycles[:]
remove_motorcycles.remove('suzuki')
print(remove_motorcycles)
