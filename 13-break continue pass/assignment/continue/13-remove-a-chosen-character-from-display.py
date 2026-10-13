# Take a string and a character. Print the string without displaying any occurrence of that character. Do not use string replacement methods; use a loop and continue.
s = input("Enter a string: ")
ch = input("ENter the character to remover: ")

for i in s:
    if i == ch:
        continue
    print(i, end = "")