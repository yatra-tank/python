# Print only odd column values for every row.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j%2 != 0:
            print(j, end= " ")
    print()