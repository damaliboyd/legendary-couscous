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


print('Is 2 greater than 3', 2 > 3)
print('Is 2 less than 3 and greater than 1', 2 < 3 and 2 > 1)

if num > flt:
    print(num, 'is greater than', flt)
elif num < flt:
    print(num, 'is less than', flt)
else:
    print (num, 'is equal to', flt)


# Lists
my_list = [4, True, 'hi'] 
shallow_copy_list = my_list # Shallow copy
new_list = my_list[:] # Deep copy

print(my_list)
print('length of list is', len(my_list))
print(my_list.pop())
print(my_list)

my_list.append('toodaloo')

print(my_list)
print(my_list.pop(0))
print(my_list)
print(my_list[0])
print('--------')
print(my_list)
print(shallow_copy_list)
print(new_list)


# Tuple - immutable list
my_tuple = ('one','pizza','isnt','enough')

print(my_tuple)
# Cannot chang values in tuple
# my_tuple[0] = 'error'

for i in my_tuple:
    print(i, end=' ')
print()

for i in range(len(my_tuple)):
    print(my_tuple[i], end=' ')
print()

for i,element in enumerate(my_tuple):
    print(i, element, sep=':',end=' ')
print()

# range(0, stop, 1)
for i in range(5):
    print(i, end=' ',)
print()

# range(start, stop, incrementBy)
for i in range(1, 10, 2):
    print(i, end=' ')
print()

# range(start, stop)
for i in range(4, 7):
    print(i, end=' ')
print()


# while loops
i = 0
while i < 5:
    print('somebody')
    i += 1
print("once told me...")