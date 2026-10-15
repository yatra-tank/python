# Take N and print the multiplication result for every pair from 1 to N.
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} x {j} = {i * j}")