# Print a star diamond.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end= "")
    for j in range(2 * i -1):
        print("*", end= "")
    print()

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()