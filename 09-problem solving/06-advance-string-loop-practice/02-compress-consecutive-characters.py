# You are given a string S. Compress consecutive repeated characters by writing the character followed by the number of times it appears consecutively.
s = input("Enter a string: ")

new_s = ""
current = s[0]
count = 1

for i in range(1, len(s)):
    if s[i] == current:
        count += 1
    else:
        new_s += current + str(count)
        current = s[i]
        count = 1

new_s += current + str(count)
print(new_s)