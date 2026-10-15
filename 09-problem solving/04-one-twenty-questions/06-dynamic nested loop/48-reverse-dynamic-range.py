# For each i, print i down to 1.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        if j > 1:
            print(j, end=" ")
        else:
            print(j, end="")
    print()
