#coding:utf-8

##=======模块==========##
#模块可以理解为一个包含了函数和变量的py文件。在你的程序中引入了某个模块，就可以使用其中的函数和变量。

import random    #import语句告诉python，我们要用random模块中的内容。

print random.randint(1,10)   #函数前加上“random.”这样python才知道你要调用random中的方法。
print random.choice([1,3,5])

#======想知道random有那些函数和变量，可以用dir()方法：
print dir(random)    

#======用到random中的某一函数或变量，可以通过from...import...指明：
from math import pi
print pi

#======将引入的方法换个名字：
from math import pi  as math_pi
print math_pi
