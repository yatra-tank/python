for i in range(5):
    print("Hello")

for i in range(10):
    print(i, end=" ")

print()

for i in range(1, 11):
    print(i, end=" ")

print()

for i in range(10, 0, -1):
    print(i, end=" ")

print()

for i in range(5, 51, 5):
    print(i, end=" ")

print()

for i in range(2, 21, 2):
    print(i, end=" ")

print()

for i in range(1, 20, 2):
    print(i, end=" ")

print()

for i in range(3, 19, 3):
    print(i, end=" ")

print()

for i in range(20, 1, -2):
    print(i, end=" ")

print()

n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    print(i, end=" ")

print()

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")

print()

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, end=" ")

print()

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")

print()

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1

print(count)

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i

print(sum)

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        sum += i

print(sum)

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)

n = int(input("Enter a number: "))

product = 1

for i in range(1, n + 1):
    product *= i

print(product)

text = input("Enter a string: ")

for ch in text:
    print(ch)

text = input("Enter a string: ")

for ch in text:
    print(ch, end="")

print()

text = input("Enter a string: ")

count = 0

for ch in text:
    count += 1

print(count)

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch == "a":
        count += 1

print(count)

text = input("Enter a string: ")

count = 0

for ch in text:
    if ch >= "A" and ch <= "Z":
        count += 1

print(count)

for i in range(3):
    for j in range(4):
        print("*", end="")
    print()

for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()