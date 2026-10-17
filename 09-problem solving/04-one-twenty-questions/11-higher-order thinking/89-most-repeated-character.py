# Find the highest-frequency character without count/ max/ set.
s = input("Enter a string: ")

highest = 0
result = ""

for i in range(len(s)):
    freq = 0

    for j in range(len(s)):
        if s[i] == s[j]:
            freq += 1

    if freq > highest:
        highest = freq
        result = s[i]

print(result)