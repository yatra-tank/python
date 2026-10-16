# Print centered odd-length number sequences.
n = int(input("Enter your number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    
    for j in range(1, 2 * i):
        print(j, end="")
    print(" ")