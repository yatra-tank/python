# Print an inverted number pyramid.
n = int(input("Enter your number: "))

for i in range(n, 0 , -1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()