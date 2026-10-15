# Take rows and columns and print every coordinate.
row = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(row):
    for j in range(cols):
        print(f"({i},{j})")
    print()