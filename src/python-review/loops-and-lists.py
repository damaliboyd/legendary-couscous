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

# slice
x = [0,1,2,3,4,5,6,7,8,9,10]
y = ['so long', 'long', 'farewell', 'au revoir', 'auf wiedersehen']
s = "You won't like me when i'm angry"

# [stop:start:step]
sliced = x[0:5:2]
print(sliced)

reversed = y[::-1]
print(reversed)

reversed = s[::-1]
print(reversed)

# List Comprehensions
x = [x for x in range(5)]
print(x)
x = [[0 for x in range(3)] for x in range(3)]
print(x)
x = [x for x in range(50) if x % 5 == 0]
print(x)

x = tuple(x for x in range(5))
print(x)