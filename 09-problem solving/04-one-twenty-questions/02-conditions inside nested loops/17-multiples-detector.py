# For every i from 1 to N, print values j from 1 to N that are multiples of i.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j%i == 0:
            print(j, end= " ")
    print()