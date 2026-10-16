# Print character pairs whose ASCII difference is greater than 5.
s = input("Enter a string: ")

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if abs(ord(s[i]) - ord(s[j])) > 5:
            print(f"({s[i]}, {s[j]})", end=" ")
print()