# You are given a string S. Find the first character that appears exactly once in the entire string. If no such character exists, print -1. Do not use dictionaries, sets, or the count() method.
s = input("EnNter a string: ")
found = False

for i in s:
    count = 0
    for j in s:
        if i == j:
            count += 1
            
    if count == 1:
        print(i)
        found = True
        break

if not found:
    print(-1)