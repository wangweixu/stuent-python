# coding:utf-8

import urllib2
web =  urllib2.urlopen('http://www.baidu.com')  #用于发送网络请求，获取数据
content = web.read()

#b=r"E:\新建文件夹\a.html"
a = open(r"E:\新建文件夹\bnn.html".decode('utf8'),'w')
a.write(content)
a.close()
