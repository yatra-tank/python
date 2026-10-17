# Compare word pairs and find the pair with maximum common characters.
s = input("Enter a string: ")
word = s.split()

max_count = 0
max_pair = ""

for i in range(len(word)):
    for j in range(i + 1, len(word)):
        count = 0

        for k in word[i]:
            for l in word[j]:
                if k == l:
                    count += 1

        if count > max_count:
            max_count = count
            max_pair = word[i] + " " + word[j]

print(max_pair)