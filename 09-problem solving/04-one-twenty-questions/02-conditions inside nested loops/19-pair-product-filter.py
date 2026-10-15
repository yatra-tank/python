# Print pairs and products only when the product is even.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i*j)%2 == 0:
            print(i, j, i*j)
            print(end="")