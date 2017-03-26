# coding:utf-8

#import urllib2
#web =  urllib2.urlopen('http://m.weather.com.cn/data5/city.xml')  #获取所有省/直辖市的编码
#DataLevel1 = web.read()

#fDataLevel1 = open(r"E:\新建文件夹\省、直辖市的编码.txt".decode('utf8'),'w')
#fDataLevel1.write(DataLevel1)
#fDataLevel1.close()


import urllib2
web =  urllib2.urlopen('http://www.weather.com.cn/data/cityinfo/101120802.html')  #获取所有省/直辖市的编码
DataLevel1 = web.read()
print DataLevel1.decode("utf-8")

fDataLevel1 = open(r"E:\新建文件夹\省、直辖市的编码.txt".decode('utf8'),'w')
fDataLevel1.write(DataLevel1)
fDataLevel1.close()
