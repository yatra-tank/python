# Compare digits of two numbers using nested loops.
s1 = input("Enter a string: ")
s2 = input("Enter another string: ")
count = 0 

for i in s1:
    for j in s2:
        if i == j:
            count += 1
print(count)