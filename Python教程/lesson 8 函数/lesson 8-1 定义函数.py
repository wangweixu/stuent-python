# coding:utf-8

print("---定义函数---")


def greet_user():
    """显示简单的问候语"""      # 文档字符串(docstring)的注释，描述函数是做什么的。
    print("hello!")


greet_user()
print("\n---向函数传递信息---")


def greet_user(uesrname):
    """显示简单的问候语"""      # 文档字符串(docstring)的注释，描述函数是做什么的。
    print("hello, " + uesrname.title() + "!")


greet_user('jesse')
