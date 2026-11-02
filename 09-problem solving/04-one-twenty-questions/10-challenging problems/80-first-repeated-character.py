# Find the first character appearing more than once.
s = input("Enter a string: ")
flag = False

for i in range(len(s)):
    for j in range(i):
        if s[i] == s[j]:
            print(s[i])
            flag = True
            break
    if flag:
        break