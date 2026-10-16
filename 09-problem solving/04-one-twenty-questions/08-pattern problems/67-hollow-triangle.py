# Print a hollow right triangle.
n = int(input("Enter your number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or i == n or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()