#coding:utf-8

print("---检查特殊元素---")
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

print("\n---检查空列表---")
requested_toppings1 = []
if requested_toppings1:
    for requested_topping1 in requested_toppings1:
        print("Adding " + requested_topping1 + ".")
else:
    print("Are you sure you want a plian pizza?")

print("\n---使用多个列表---")
available_toppings = ['mushroom','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings2 = ['mushroom','french fries','extra cheese']
for requested_topping2 in requested_toppings2:
    if requested_topping2 in available_toppings:
        print("Adding " + requested_topping2 + ".")
    else:
        print("Sorry, we don't have " + requested_topping2 + ".")
print("\nFinished making your pizza!")