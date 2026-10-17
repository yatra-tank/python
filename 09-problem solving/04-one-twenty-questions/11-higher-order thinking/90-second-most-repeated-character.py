# Find the second-highest frequency character and handle ties.
s = input("Enter a string: ")

highest = 0
second = 0
result = ""

for i in range(len(s)):
    freq = 0

    for j in range(len(s)):
        if s[i] == s[j]:
            freq += 1

    if freq > highest:
        second = highest
        highest = freq
        result = ""

    elif freq < highest and freq > second:
        second = freq
        result = s[i]

    elif freq == second:
        if result == "":
            result = s[i]

print(result)