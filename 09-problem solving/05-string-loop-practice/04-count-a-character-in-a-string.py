# You are given a string S and a character C. Count how many times character C appears in S.
s = input("Enter a string: ")
c = input("Enter a character: ")
count = 0

for i in s:
    if i == c:
        count += 1

print(count)