# For every prime up to N, display its factors.
n = int(input("Enter a number: "))

for i in range(2, n + 1):
    print(i, "->", end= " ")
    for j in range(1, i + 1):
        if i%j == 0:
            print(j, end= " ")
    print()