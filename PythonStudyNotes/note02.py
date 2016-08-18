# -*- coding:utf-8 -*-
# Tuple
# The item in the tuple can't modify , visited only,it's data type isn't limited.
tuple = ('a string',False,2.5,34)

print tuple
print type(tuple) # print: <type 'tuple'>
print tuple[0]
print tuple[1]
print tuple[2]
print tuple[3]
#print tuple1[4] # Will throw an Index Error:tuple index out of range
print 


# List
# The item in the list can be modified and visited, it's data type isn't limited.
list = [True,45,'This is a good day!']
print list
print type(list) #print:<type 'list'>
print list[0]
print list[1]
print list[2]
#print list[4] # Will throw an Index Error:tuple index out of range
print

anotherlist = [1,[2,3,4],True]
print anotherlist
print anotherlist[1][1] #print : 3
print 

emptylist = []
print emptylist
print

tuplewithlistitemcannotmodifyalso = ('a string',False,2.5,34,(2,3,'str'),[True,'asdf'])
#tuplewithlistitemcannotmodifyalso[4][0] =False # can't modify also.
print tuplewithlistitemcannotmodifyalso