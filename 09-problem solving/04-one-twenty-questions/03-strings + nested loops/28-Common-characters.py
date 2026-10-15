# Print characters occurring in both strings without using set().
s1 = input("Enter a string: ")
s2 = input("Enter another string: ")
empty_s = ' '

for i in s1:
    for j in s2:
        if i == j:
            if i in empty_s:
                continue
            empty_s += i
                    
            print(i)
            print(end= "")