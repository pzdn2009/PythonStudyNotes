# if

i = 3
if i == 1:
    print i
elif i == 3:
    print 3
else:
    print 2

print

#for
for a in [3,9,True,'pzdn2009']:
    print a

print
#while
i = 1
while i < 10:
    i = i + 1
    if i == 2:
        continue
    if i == 4:
        break
    print i

print
# function
# () is value type,[] is reference type.
def get_result(a,b):
    return (a,b,a + b)

print get_result(4,5)