# [from:to:step] : get sub range from tuple or list.
""" 
  step: default is 1 , if there's a negative sign , indicates the travel direction is from right to left.
  from :the start index of the range,include it;
  to:the end index of the range,exclude it.

  if there's negetive sign before 'from(to)' , indicates the number direction is from right to left.

  string is type of tuple.

  when add an item to the list , need 
"""

t = (2,1.3,'love',5.6,9,12,False)
l = [True,5,'smile']

print t == t[:] # True
print t[:5] #(2,1.3,'love',5.6,9)
print l[2:] #['smile']
print l[0:5:2] #[True,'smile']
print t[2:0:-1] #(1.3,'love')
print l[-1]
print l[1] == l[-2]

#append an item
l.append('pzdn2009')
print l[-1] == 'pzdn2009'

#string
str = 'abcdef'
print str[2:4],type(str)
print 
#Math,Condition,Logic
"""
Math: +, -, *, /, **, %
Condition: ==, !=, >, >=, <, <=, in
Logic: and, or, not
"""

print 3**4
print 5 in [1,3,5]
print 
print True and False
print True or False
print not True