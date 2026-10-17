# Find the character with the highest matching frequency between two strings.
s1 = input("Enter a string:")
s2 = input("Enter another string:")

max_count = 0
max_ch = "" 

for i in range(len(s1)):
    count = 0

    for j in range(len(s2)):
        if s1[i] == s2[j]:
            count += 1

    if count > max_count:
        max_count = count
        max_ch = s1[i]

print(max_ch)