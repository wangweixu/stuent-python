# coding:utf-8

print("---位置实参---")


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

print("---关键字实参---")
describe_pet(animal_type='dog', pet_name='willie')  # 给形参animal_type给赋值了'dog'，形参pet_name给赋值了'willie'
describe_pet(pet_name='willie', animal_type='dog')

print("---默认值---")


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')  # 给形参animal_type指定了默认值'dog'，形参pet_name给赋值了'willie'
describe_pet('willie')
describe_pet(animal_type='hamster', pet_name='harry')
# 给形参animal_type给赋值了'hamster'，形参pet_name给赋值了'harry'
describe_pet('harry', 'hamster')
