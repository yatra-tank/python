# For every pair, print the pair and absolute ASCII difference.
s = input("Enter a string: ")

for i in s:
    for j in s:
        print(f"{i} {j} -> {abs(ord(i) - ord(j))},", end= " ")
    print()