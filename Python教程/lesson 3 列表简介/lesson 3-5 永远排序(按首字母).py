#coding:utf-8
cars = ['bmw','audi','toyota','subaru']

print("----使用sort()对列表进行永远排序，按首字母顺序排列---")
cars1 = cars[:]
cars1.sort()
print(cars1)

print("\n----使用sort()对列表进行永远排序，按首字母顺序相反的顺序排列---")
cars2 = cars[:]
cars2.sort(reverse=True)
print(cars2)
