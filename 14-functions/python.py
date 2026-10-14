a = 10
b = 20
c = 40
d = 50

def add(a, b):
    c = a + b
    return c

def sub(a, b):
    return a - b

def floor_division(a, b):
    return a // b

print(floor_division(sub(add(a, b), c), d))