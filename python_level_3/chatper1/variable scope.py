# Keyword - scope, global, nonlocal, locals, globals
# EX1
a = 10 # Global variable

def foo():
    # Read global variable
    print('EX1 >', a)

foo()
# Read global variable
print('EX1 >', a)

# EX2
b = 20
def bar():
    b = 30 # Local variable
    print('EX2 >', b) # Read local variable

bar()
print('EX2 >', b) # Read global variable

# EX3
c = 40

def foobar():
    # c = c + 10 UnboundLocal Error
    # c = 10
    # c += 100
    print('EX3 >', c)

foobar()

# EX4
d = 50
def barfoo():
    global d
    d = 60
    d += 100
    print('EX4 >', d)

barfoo()

print('EX4 >', d)

# EX5
def outer():
    e = 70
    def inner():
        nonlocal e
        e += 10
        print('EX5 >', e)
    return inner

in_test = outer() # Closure

in_test()
in_test()

# EX6
def func(var):
    x = 10
    def printer():
        print('EX6 >', "Printer Func Inner")
    print('Func Inner', locals()) # 지역 전체 출력

func('Hi')

# EX7
print('EX7 >', globals()) # 전역 전체 출력
globals() ['test_variable'] = 100
print('EX7 >', globals())

# EX8(지역 -> 전역 변수 작성)
for i in range(1, 10):
    for k in range(1, 10):
        globals() ['plus_{}_{}'.format(i,k)] = i + k

print(globals())
print(plus_3_5)