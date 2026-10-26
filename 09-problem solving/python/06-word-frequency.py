s1 = input("Enter a string: ")
s2 = input("Enter the word: ")

j = 0

for i in s1:
    if j < len(s2):
        if i == s2[j]:
            j = j + 1

if j == len(s2) and j != 0:
    print("found")
else:
    print("not found")