# Python Review
[Python As Fast as Possible - Learn Python in ~75 Minutes](https://www.youtube.com/watch?v=VchuKL44s6E)
- Python is general purpose programming langauge
- Simple to read and develop with
- Typically used with Web dev, ML, and data science tasks

- DataTypes
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

- Printing
    - `print("Hello World")`
    - `print(4.5, "is a number")` autmatically adds space in between
    - `print("str", end='')` passing end argument will override end character, the default is newline '\n'

    ```
    # Input and Output
    print(num + flt)
    name =  input('Name: ')
    print(str, name)
    print(str * 3, name)
    age = int(input('How old are ye?'))
    ```
- Variables - no special characters in variables(other then _) or starting with number
    - use snake case test_var_example

- user input with `input(Name:)` returns all data as string

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
## Lists
```
# Lists
my_list = [4, True, 'hi'] 
shallow_copy_list = my_list # Shallow copy
new_list = my_list[:] # Deep copy

print(my_list)
print('length of list is', len(my_list))
print(my_list.pop()) // .pop() removes last item and returns it
print(my_list)

my_list.append('toodaloo') // why is there not a push?!?

print(my_list)
print(my_list.pop(0)) // index can be passed to pop()
print(my_list)
// Lists store references to data and can be referenced like arrays
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
```