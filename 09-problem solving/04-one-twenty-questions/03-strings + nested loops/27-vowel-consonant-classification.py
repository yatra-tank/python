# Compare each character against AEIOUaeiou using a nested loop.
s = input("Enter a string: ")

for i in s:
    is_vowel = False

    for j in 'aeiouAEIOU':
        if i == j:
            is_vowel = True
            break

    if is_vowel:
        print(f" {i} = Vowel")
    else:
        print(f" {i} = Consonant")