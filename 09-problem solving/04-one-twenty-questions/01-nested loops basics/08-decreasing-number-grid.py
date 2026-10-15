# Take N and print 1..N, then one fewer number on every row.
n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end= " ")
    print()