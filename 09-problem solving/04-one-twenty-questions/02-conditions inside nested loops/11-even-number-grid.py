# Print only even column values for every row.
row = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(1, row + 1):
    for j in range(1, cols + 1):
        if j%2 == 0:
            print(j, end= " ")
    print()