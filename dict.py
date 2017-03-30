# coding=utf-8
key = [1, 2, 3]
s = 'demo'
print type(key), type(s)

dict1 = {1: 'demo', 2: 'ankle'}
print dict1[1]
dict2 = {2: 'ankle', 1: 'demo'}
print dict2, dict2.get(3)

if 5 < 6:
    print 'true'

newInput = input('输入age:')
if newInput>18:
    print '成年'
else:
    print '未成年'

print newInput
print newInput
