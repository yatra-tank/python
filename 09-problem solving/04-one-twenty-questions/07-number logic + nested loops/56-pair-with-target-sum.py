# Print all pairs from 1..N whose sum equals target.
n = int(input("Enter a number: "))
target = int(input("Enter a target: "))
sum = 0 

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum = i + j

        if sum == target:
            print(i, j)