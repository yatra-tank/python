# Print seat labels using alphabet rows and numeric columns.
rows = int(input("Enter number of rows: : "))
cols = int(input("Enter number of columns: "))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(f"{chr(64 + i)}{j}", end=" ")
    print()