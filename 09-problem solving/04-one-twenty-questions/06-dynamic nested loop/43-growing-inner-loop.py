# For each i from 1 to N, run inner loop 1..i.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end= " ")
    print()