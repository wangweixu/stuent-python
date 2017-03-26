# coding:utf-8

f=file("E:\Python imformation\scores.txt")
lines = f.readlines()
#print lines
f.close()

results = []      #在循环之前初始化results
#print results
for line in lines:
    data = line.split()   #对每一条数据进行处理。按照空格，把姓名、成绩分割开
    #print data
    
    sum = 0
    for socre in data[1:]:
        point = int(socre)
        if point < 60:
            continue     #小于60分则略过本次循环，不累加小于60分的值
        sum +=int(socre)
    result = '%s\t: %d\n'%(data[0],sum)
    #print result

    results.append(result)   #得到一个学生的总成绩之后，把它添加都一个list中
#print results
output = file("E:\Python imformation\scores1.txt",'w')
output.writelines(results)
output.close()
