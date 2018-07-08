#encoding:utf-8
line = 60

def fun(num):
    line = 30
    if num > line:
        return u'大'
    else:
        return u'小'

print fun(50)
print line