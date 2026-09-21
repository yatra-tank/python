s = input("Enter a sentence: ")
words = s.split()

highest_word = ""
highest_score = -1

for i in words:
    count = 0

    for j in i:
        if j.lower() in "aeiou":
            count += 2
        elif j.isalpha():
            count += 1
        elif j.isdigit():
            count += 3
        else:
            count += 4

    print(i, count)

    if count > highest_score:
        highest_score = count
        highest_word = i

print("Highest scoring word:", highest_word)