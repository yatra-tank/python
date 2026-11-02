# Find repeated words in a sentence without count().
s = input("Enter a string: ")
words = s.split()

for i in range(len(words)):
    
    flag = False
    for k in range(i):
        if words[i] == words[k]:
            already_printed = True
            break
            
    if flag:
        continue

    is_duplicate = False
    for j in range(i + 1, len(words)):
        if words[i] == words[j]:
            is_duplicate = True
            break 

    if is_duplicate:
        print(words[i])