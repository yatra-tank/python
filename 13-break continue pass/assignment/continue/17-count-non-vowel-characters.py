# Take a word and count how many characters are not vowels. Use continue to skip vowels.
s = input("Enter a word: ")
count = 0

for i in s:
    if i in "aeiou":
        continue

    count += 1

print(count)