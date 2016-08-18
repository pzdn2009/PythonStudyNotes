# List's Methods
print dir(list)
#print help(list)

l = [1,3,5,7]
l.append('pzdn2009')

l.append(3)
print l
print l.count(3)
print l.index('pzdn2009')

l.insert(0,12)
print l

print l.pop(2)
print l

print l.pop()
l.reverse()
print l

l.sort()
print l

print [1,2,3] + [5,6,9] # contact two lists

print dir(dict)