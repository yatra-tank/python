# Take rows and columns and print a rectangle of *.
row = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

for i in range(1, row + 1):
    for j in range(1, cols + 1):
        print("*", end= " ")
    print()