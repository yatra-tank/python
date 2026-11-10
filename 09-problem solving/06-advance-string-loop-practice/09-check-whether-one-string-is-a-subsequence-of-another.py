# You are given two strings, S and P. Check whether all characters of P appear in S in the same order. The characters do not need to be next to each other.
s = input("Enter a string: ")
p = input("Enter a character: ")

i, j = 0, 0

while i < len(s) and j < len(p):
    if s[i] == p[j]:
        j += 1
    i += 1

if j == len(p):
    print("yes")
else:
    print("no")