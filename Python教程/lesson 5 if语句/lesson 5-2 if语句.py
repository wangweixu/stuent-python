# coding:utf-8

print('---if语句---')
age = 19
if age >= 18:
    print("You are old enough to wotel")

print('\n---"if-elif-else"语句---')  # 对单个代码块，若多个代码块，则要使用一系列单独的if语句。
age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 6
print("Your admission cost is $"+str(price)+".")
