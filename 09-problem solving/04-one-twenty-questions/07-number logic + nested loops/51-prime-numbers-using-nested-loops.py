# Find all primes from 2 to N.
n = int(input("Enter a number: "))

for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break 
    else:
        print(i, end=" ")
print()