# You are given two strings, S and P. Count how many times P occurs inside S.
s = input("Enter a string: ").strip()
p = input("Enter a character: ").strip()

count = 0

for i in range(len(s) - len(p) + 1):
    sub = ""
    for j in range(len(p)):
        sub += s[i + j]
    print(sub)
#     if sub == p:
#         count += 1

# print(count)