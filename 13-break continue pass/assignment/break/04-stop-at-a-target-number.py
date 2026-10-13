# Take an integer limit. Print numbers from 1 through limit, but stop before printing 7. If limit is less than 7, print all numbers up to limit.
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i == 7:
        break
    print(i, end=" ")