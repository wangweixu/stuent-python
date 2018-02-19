print 'a'
a = input()
print 'b'
b = input()
if a > 0:
    if b > 0:
        print '01'
    elif b < 0:
        print "02"
    else:
        print "03"
elif a < 0:
    if b > 0:
        print 11
    elif b < 0:
        print 12
    else:
        print 13
else:
    if b > 0:
        print 21
    elif b < 0:
        print 22
    else:
        print 23
