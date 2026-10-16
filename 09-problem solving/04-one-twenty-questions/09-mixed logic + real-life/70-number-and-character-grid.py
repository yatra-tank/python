# Combine characters from a word with column numbers.
s = input("Enter a string: ")
n = int(input("Enter number of columns: "))

for i in range(len(s)):
    for j in range(1, n + 1):
        print(f"{s[i]}{j}", end=" ")
    print()