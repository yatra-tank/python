# 1. Print "Hello" five times

for i in range(5):
    print("Hello")


# 2. Print 0 to 9

for i in range(10):
    print(i, end=" ")


# 3. Print 1 to 10

for i in range(1, 11):
    print(i, end=" ")


# 4. Print 10 to 1

for i in range(10, 0, -1):
    print(i, end=" ")


# 5. Print 5 to 50 increasing by 5

for i in range(5, 51, 5):
    print(i, end=" ")


# 6. Even numbers from 2 to 20

for i in range(2, 21, 2):
    print(i, end=" ")


# 7. Odd numbers from 1 to 19

for i in range(1, 20, 2):
    print(i, end=" ")


# 8. Print 3, 6, 9, 12, 15, 18

for i in range(3, 19, 3):
    print(i, end=" ")


# 9. Print 20 down to 2 by 2

for i in range(20, 1, -2):
    print(i, end=" ")


# 10. Print 1 to n

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i, end=" ")


# 11. Even numbers from 1 to n

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")


# 12. Odd numbers from 1 to n

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")


# 13. Numbers divisible by 3

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, end=" ")


# 14. Numbers divisible by both 2 and 3

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")


# 15. Count even numbers from 1 to n

n = int(input("Enter n: "))
count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count = count + 1

print(count)


# 16. Sum 1 to n

n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print(sum)


# 17. Sum of even numbers from 1 to n

n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum + i

print(sum)


# 18. Sum of odd numbers from 1 to n

n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        sum = sum + i

print(sum)


# 19. Multiplication table

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n * i)


# 20. Factorial: 1 × 2 × ... × n

n = int(input("Enter n: "))
product = 1

for i in range(1, n + 1):
    product = product * i

print(product)


# 21. Print each character on a separate line

string = input("Enter string: ")

for i in string:
    print(i)


# 22. Print all characters on same line

string = input("Enter string: ")

for i in string:
    print(i, end="")


# 23. Count number of characters

string = input("Enter string: ")
count = 0

for i in string:
    count = count + 1

print(count)


# 24. Count number of "a"

string = input("Enter string: ")
count = 0

for i in string:
    if i == "a":
        count = count + 1

print(count)


# 25. Count uppercase letters
# Using a known set of uppercase characters

string = input("Enter string: ")
count = 0

for i in string:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count = count + 1

print(count)


# 26. Print 3 rows of 4 stars

for i in range(3):
    for j in range(4):
        print("*", end="")
    print()


# 27. Print 4 rows of 5 stars

for i in range(4):
    for j in range(5):
        print("*", end="")
    print()


# 28. Star triangle

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


# 29. Number triangle

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 30. Multiplication table grid from 1 to 5

for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()


# FINAL CHALLENGE

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()