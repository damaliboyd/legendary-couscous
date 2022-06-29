"""
Python doesnt really have multiline comments...
But using a multiline string not set to anything
is a pretty close second
"""

# DataTypes
num = 123
flt = 12.30
str = 'hello'
bool = True

# Input and Output
print(num + flt)
name =  input('Name: ')
print(str, name)
print(str * 3, name)
age = int(input('How old are ye?'))

# Opertors
print('Is 2 greater than 3', 2 > 3)
print('Is 2 less than 3 and greater than 1', 2 < 3 and 2 > 1)

if num > flt:
    print(num, 'is greater than', flt)
elif num < flt:
    print(num, 'is less than', flt)
else:
    print (num, 'is equal to', flt)