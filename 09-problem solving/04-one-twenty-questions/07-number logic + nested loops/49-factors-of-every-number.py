# Print all factors of every number from 1 to N.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i,"->", end= " ")
    for j in range(1, i + 1):
        if i % j == 0:
            print(j, end=" ")
    print()