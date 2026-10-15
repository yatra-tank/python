# Take N and print an N×N grid where columns alternate between 0 and 1.
n = int(input("Enter a number:  "))

for i in range(1, n + 1):
    for j in range(1, n +1):
        if j%2 == 0:
            print("1", end= " ")
        else:
            print("0", end= " ")
    print()
