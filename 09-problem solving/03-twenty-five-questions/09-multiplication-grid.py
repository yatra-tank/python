n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()