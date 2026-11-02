# Find characters occurring more than once without count() or set().
s = input("Enter a string: ")
unique = ""
duplicate = ""

for i in s:
    if i in unique:
        if i in duplicate:
            continue

        if duplicate == "":
            duplicate += i
        else:
            duplicate += ", " + i
    else:
        unique += i

print("Repeated characters: ", duplicate)