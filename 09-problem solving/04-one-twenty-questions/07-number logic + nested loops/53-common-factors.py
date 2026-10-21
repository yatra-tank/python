# Find common factors of A and B using nested loops.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if i == j:
            if a % i == 0 and b % j == 0:
                print(i, end=" ")