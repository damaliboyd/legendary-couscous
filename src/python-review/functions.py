# Functions
def func():
    print('Run')

func()

def add(x=0,y=0):
    return x + y

print('add(1,2) =', add(1,2))
print('add(7) =', add(7))
print('add() =', add())

def returnItems():
    return 42,48,57

i1,i2,i3 = returnItems()

print(i1,i2,i3)

def func01(x):
    def func02():
        print(x)

    return func02

func01(4)()
testFunc02 = func01(420)
testFunc02()


def a(x):
    def b():
        def c():
            def d():
                print(x)
            d()
        c()
    b()

a(1337)

# Unpack operator
x = [1, 23, 42, 345, 3889595]
print(*x)

def printPair(x,y):
    print(x,y)

pairs = [(1,2),(3,4)]

for pair in pairs:
    printPair(*pair)

printPair(**{'x': 2,'y':5})

# args are postional arguments
# kwards are keyword/named arguments
def func(*args, **kwargs):
    print(*args)
    print(kwargs)
    a,b = kwargs
    print(a,b)
    print(kwargs[a],kwargs[b])

func(1,2,3,4,5,6,{'x': 2,'y':5},one=0,two=1)

# Scopes
g = 'tim'

def func(verb):
    global g # Never use global
    g = 'tiny ' + g + ' ' + verb

print(g)
func('lives')
print(g)

# # Exceptions
# raise Exception('Bad')
# raise FileExistsError('This file has already been created. Yeet it or rename.')

try:
    x = 7 / 0
except Exception as e:
    print('Cant divide by 0')
finally:
    print('finally always runs')

# lamdas
x = lambda x: x + 5
print(x(4))

x = [1,2,3,4,5,3,3,21,2,313,1,23,142,4]
mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

# f string
x = f'hello {6+8}'
print(x)