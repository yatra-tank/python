# Run inner loop i times and print only even inner values.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, 2 * i - 1):
        if j%2 == 0:
            print(j, end= " ")
    print()