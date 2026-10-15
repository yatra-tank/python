# Print all pairs from 1 to N whose sum is greater than N.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) > n:
            print(i, j)
            print(end="")