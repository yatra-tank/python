# Take an integer n. Print numbers from 1 to n, skipping multiples of 3.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")