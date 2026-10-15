# Print pairs where first character is vowel and second is consonant.
s = input("Enter a string: ")

for i in s:
    for j in s:
        if i in 'aeiouAEIOU' and j not in 'aeiuoAEIOU':
            print(f"{i}-{j},", end= " ")