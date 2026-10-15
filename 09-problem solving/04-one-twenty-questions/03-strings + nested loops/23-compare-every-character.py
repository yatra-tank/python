# Compare every character with every other character and label Same/Different.
s = input("Enter a string: ")
empty_s = ' '

for i in s:
    for j in s:
        if i == j:
            print("Same", end= " ")
        else:
            print("Different", end= " ")
        print()