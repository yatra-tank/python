# Print centered repeated row numbers.
n = int(input("Enter your number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    
    for j in range(1, 2 * i):
        print(i, end="")
    print(" ")