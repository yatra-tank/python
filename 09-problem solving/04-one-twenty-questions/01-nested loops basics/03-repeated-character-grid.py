# Take a character, rows and columns. Print the character as a rectangle.
s = input("Enter your charcter: ")
row = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(1, row + 1):
    for j in range(1, cols + 1):
        print(s, end= " ")
    print()