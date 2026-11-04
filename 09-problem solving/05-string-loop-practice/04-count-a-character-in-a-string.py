# You are given a string S and a character C. Count how many times character C appears in S. The comparison is case-sensitive. For example, A and a are different characters.
s = input("Enter a string: ")
c = input("Enter your character: ")
count = 0

for i in s:
    if i == c:
        count += 1

print(count)