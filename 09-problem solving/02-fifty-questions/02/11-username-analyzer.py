for i in range(5):
    s = input("Enter a username: ").strip()

    digit = 0
    underscore = 0
    special = 0

    for j in s:
        if j.isdigit():
            digit += 1
        elif j == "_":
            underscore += 1
        elif not j.isalnum() and not j.isspace():
            special += 1

    length = len(s)
    first_char = s[0]

    if length >= 8 and first_char.isalpha() == True and digit > 0 and special == 0:
        print("valid")
    elif special > 0 or first_char.isalpha() == False:
        print("Invalid")
    else:
        print("Needs Improvement")