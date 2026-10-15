# For each character, count its occurrences using nested loops.
s = input("Enter a string: ")
empty_s = ' '

for i in s:
    if i in empty_s:
        continue
    empty_s += i
    count = 0

    for j in s:
        if j == i:
            count += 1
                
    print(i, count)
    print(end= "")