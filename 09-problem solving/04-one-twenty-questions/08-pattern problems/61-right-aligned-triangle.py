# Print a right-aligneed star triangle.
n = int(input("Enter your number: "))

for i in range(1, n + 1): 
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end= "")
    print("")