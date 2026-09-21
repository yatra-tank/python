s = input("Enter a string: ")

vowel = 0
consonant = 0
digit = 0
special = 0

for i in range(len(s)):
    j = s[i]

    if (i + 1) % 2 == 0:
        pos = "Even"
    else:
        pos = "Odd"

    if j.lower() in "aeiou":
        category = "Vowel"
        vowel += 1
    elif j.isalpha():
        category = "Consonant"
        consonant += 1
    elif j.isdigit():
        category = "Digit"
        digit += 1
    else:
        category = "Special"
        special += 1

    print(j, i + 1, pos, category)

print("Vowels:", vowel)
print("Consonants:", consonant)
print("Digits:", digit)
print("Special:", special)