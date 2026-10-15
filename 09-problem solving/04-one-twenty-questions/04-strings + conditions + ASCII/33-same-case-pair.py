# Print pairs whose two characters have the same case.
s = input("Enter a string: ")

for i in s:
    for j in s:
        if i.isupper() and j.isupper() or i.islower() and j.islower():
            print(f"{i},{j}")   