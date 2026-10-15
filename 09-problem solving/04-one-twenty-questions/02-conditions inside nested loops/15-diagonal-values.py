# Create an N×N grid with 1 on the main diagonal and 0 elsewhere.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("1", end= " ")
        else:
            print("0", end= " ")
    print()