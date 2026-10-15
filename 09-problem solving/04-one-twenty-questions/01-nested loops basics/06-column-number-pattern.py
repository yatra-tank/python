# Take N and print 1 to N in every row.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end= " ")
    print()