# Take N and print 1, then 12, then 123, and so on.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end= " ")
    print()