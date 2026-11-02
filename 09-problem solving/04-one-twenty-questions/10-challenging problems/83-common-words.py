#  Find the words occuring in both sentences.
s1 = input("Enter a string: ")
s2 = input("Enter another string: ")
empty_s = ""

for i in s1.split():
    for j in s2.split():
        if i == j and i not in empty_s:
            empty_s += i + " "

print(empty_s)