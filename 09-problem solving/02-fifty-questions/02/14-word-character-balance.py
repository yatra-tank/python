s = input("Enter a string: ")

for i in s.split():
    vowel = 0
    consonant = 0

    for j in i:
        if j in 'aeiouAEIOU':
            vowel += 1
        else:
            consonant += 1

    print("The number of vowels are:", vowel)
    print("The number of consonants are:", consonant)

    if vowel > consonant:
        print("Vowel Heavy")
    elif vowel < consonant:
        print("Consonant Heavy")
    else:
        print("Balanced")