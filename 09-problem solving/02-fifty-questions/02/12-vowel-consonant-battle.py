s = input("Enter a string: ")

vowel = 0
consonant = 0

for i in s:
    if i in 'aeiouAEIOU':
        vowel += 1
    elif i not in 'aeiouAEIOU':
        consonant += 1

print("The number of vowels are: ", vowel)
print("The number of consonants are: ", consonant)

if vowel > consonant:
    print("Vowels Win")
elif vowel < consonant:
    print("Consonants Win")
elif vowel == consonant:
    print("Draw")
else:
    print("Try Again")