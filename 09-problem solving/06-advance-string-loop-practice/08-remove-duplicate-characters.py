# You are given a string S. Create a new string by keeping only one character from each group of consecutive repeated characters.
s = input("Enter a string: ")

res = s[0]

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        res += s[i]

print(res)