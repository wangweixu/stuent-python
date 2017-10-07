# coding:utf-8

print("---返回值---")


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()    # 在函数中，可使用retrun语句将值返回到调用函数的代码行。


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print("\n---返回字典---")


def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print("---结合使用函数和while循环---")


def get_formatted_name(first_name, last_name, middle_name):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("（enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    m_name = input("Middle_ name: ")
    if m_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name, m_name)
    print("\nHello, " + formatted_name + "!")
