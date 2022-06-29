# Python Review
[Python As Fast as Possible - Learn Python in ~75 Minutes](https://www.youtube.com/watch?v=VchuKL44s6E)
- Python is general purpose programming langauge
- Simple to read and develop with
- Typically used with Web dev, ML, and data science tasks
- Strong types will be missed

## DataTypes
- Int: `1213` or `-14`
- Float: `34.0` or `-476.0345` has max 13 decimal points
- String: `''` or `'hello world'` or `"hello world"`
    - Methods: upper, capitalize, count
    - String  multiplied by integer is a thing
- Bool: `True` or `False`
- get type with `type()`

```
num = 123
flt = 12.30
str = 'hello'
bool = True
```

## Input and Outputs
- `print("Hello World")`
- `print(4.5, "is a number")` autmatically adds space in between
- `print("str", end='')` passing end argument will override end character, the default is newline '\n'
- Variables - no special characters in variables(other then _) or starting with number
    - use snake case test_var_example

- user input with `input()` returns all data as string
```
# Input and Output
print(num + flt)
name =  input('Name: ')
print(str, name)
print(str * 3, name)
age = int(input('How old are ye?'))
```

## Operators
- Standard math operaters +, -, /, //, %,   
    - uses PEMDAS
    -  `/` division returns float can cast with int `int(9/3)`
    - `//` integer division -  it drops the values after the decimal

- Conditional operators and, or, not
```
# Operators
print('Is 2 greater than 3', 2 > 3)
print('Is 2 less than 3 and greater than 1', 2 < 3 and 2 > 1)

```
## Lists and Tuples
- Lists are mutable
    - Methods: append(value), insert(value, index), pop(), pop(index)
- Tuples are immutable and must be completely reassigned to 'change' its value
```
# Lists
my_list = [4, True, 'hi'] 
 # Shallow copy
shallow_copy_list = my_list
# Deep copy
new_list = my_list[:] 

# Get length of list
len(my_list)

# .pop() removes last item and returns it
# index can be passed to pop()
print(my_list.pop()) 
print(my_list.pop(0)) 

# why is there not a push?!?
my_list.append('toodaloo') 


# Lists store references to data and can be referenced like arrays
print(my_list[0]) 


# Tuple - immutable list
my_tuple = ('one','pizza','isnt','enough')

print(my_tuple)
# Cannot chang values in tuple
# my_tuple[0] = 'error'
```
## Loops
- the lack of parenthesis throw me off every time
- Has fancy for loops and while loops
- for in loops for collections 
- enumerate(list) can be used to iterate over collection and have the index available
```
# 
for i in my_tuple:
    print(i, end=' ')
print()

for i in range(len(my_tuple)):
    print(my_tuple[i], end=' ')
print()

for i, element in enumerate(my_tuple):
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
```