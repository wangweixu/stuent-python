# coding:utf-8

def city():
## ========获取所有省/直辖市的编码===
        import urllib2
        url1 = 'http://m.weather.com.cn/data5/city.xml'
        content1 =  urllib2.urlopen(url1).read()
        #print content1.decode("utf-8")
        provinces = content1.split(',')

        result = 'city = {\n'
        cities2 = 'city = {\n'
##========获取每个省的城市的编码===
        a = 1
        url = 'http://m.weather.com.cn/data5/city%s.xml'
        for p in provinces:
                p_code = p.split('|')[0]
                # print p_code.decode("utf-8")
                url2 = url % p_code
                content2 =  urllib2.urlopen(url2).read()
                #print content2.decode("utf-8")
                cities = content2.split(',')
##========获取每个城市的县区的编码===##
                for c in cities:
                        c_code = c.split('|')[0]
                        url3 = url % c_code
                        content3 =  urllib2.urlopen(url3).read()
                        #print content3.decode("utf-8")
                        districts = content3.split(',')
##========获取国家编码===##
                        for d in districts:
                                a+=1
                                #print a
                                d_pair = d.split('|')
                                d_code = d_pair[0]
                                name = d_pair[1]
                                cities1 = "'%s':'%s',\n"%(name,d_code)
                                cities2 +=cities1
                                f = file(r"E:\新建文件夹\cities.txt".decode('utf-8'),'w')
                                f.write(cities2)
                                f.close()

                                url4 = url % d_code
                                content4 =  urllib2.urlopen(url4).read()
                                #print content4
                                code = content4.split('|')[1]
                                line = "'%s':'%s',\n"%(name,code)
                                result +=line
                                #print name.decode("utf-8")+' : '+code.decode("utf-8")
                                result += '}'
                                f = file(r"E:\新建文件夹\districts.txt".decode('utf-8'),'w')
                                f.write(result)
                                f.close()
