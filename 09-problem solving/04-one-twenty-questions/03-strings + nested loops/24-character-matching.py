# Compare every character of two strings and print equal pairs.
s1 = input("Enter a string: ")
s2 = input("Enter another string: ")

for i in s1:
    for j in s2:
        if i == j :
            print(i, j, end= " ")
    print()