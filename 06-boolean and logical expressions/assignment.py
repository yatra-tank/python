print(True)
print(type(True))

print(False)
print(type(False))

print(True == "True")

age = 20
print(age >= 18)

marks = 45
print(marks == 50)

age = 20
print(age >= 18)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

age = 25
print(age >= 18 and age <= 60)

age = 16
print(age < 18 or age > 60)

age = 20
print(not age < 18)

num = int(input("Enter a number: "))
print(num > 10 and num < 50)

num = int(input("Enter a number: "))
print(num < 10 or num > 100)

num = int(input("Enter a number: "))
print(not num > 10)

print(bool(0))
print(bool(10))
print(bool(""))
print(bool("Hello"))
print(bool(None))

values = [0, 1, "", "Python", False, None]

for value in values:
    print(value, type(value), bool(value))