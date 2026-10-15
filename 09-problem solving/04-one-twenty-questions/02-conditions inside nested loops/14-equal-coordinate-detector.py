# For every pair from 1 to 5, print Same when i==j, otherwise Different.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("Same", end= " ")
        else:
            print("Different", end= " ")
    print()