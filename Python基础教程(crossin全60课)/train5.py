#coding:utf-8
i = 0
while i <5:
    i+=1
    for j in range(4):
        print "%d--j"%j
        if j == 2:
            break      #j=2，循环跳出
    for k in range(4):
        if k == 2:
            continue   #略过k=2
        print "%d~~k"%k
    if i > 3:
        break         #i>3,循环跳出
    print "%d&&i"%i
