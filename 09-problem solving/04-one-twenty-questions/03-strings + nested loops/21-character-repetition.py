# For every character, print it three times.
s = input("Enter a string: ")

for i in range(len(s)):
    for j in range(len(s)):
        print(s[i], end= " ")
    print()