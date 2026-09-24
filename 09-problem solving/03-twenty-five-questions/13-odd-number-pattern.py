n = int(input("Enter your number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print("")