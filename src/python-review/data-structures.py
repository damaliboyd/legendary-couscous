# Sets
x = set()
y = {4, 32, 2, 2}
print(y)
y.add(42)
y.remove(2)
print(y)

# check if item in set
print(42 in x)
print(42 in y)

# Dictionary
x = {'key': 'value', 'test':'ing'}
print(x)
x['and i'] = 'oop'
print(list(x.keys()))
print(x.values())

del x['and i']
print(x)