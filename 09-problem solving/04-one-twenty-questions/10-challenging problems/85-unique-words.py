# Print words occuring exactly once.
s = input("Enter a string: ")
words = s.split()

for i in range(len(words)):
    flag = True

    for k in range(i):
        if words[i] == words[k]:
            flag = False
            break

    if not flag:
        continue

    is_unique = True

    for j in range(i + 1, len(words)):
        if words[i] == words[j]:
            is_unique = False
            break

    if is_unique:
        print(words[i], end= " ")