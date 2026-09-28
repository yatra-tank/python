while True:
    s = input("Enter the password: ")

    length = len(s)
    upper = 0
    lower = 0
    digit = 0
    special = 0

    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
        else:
            special += 1

    if length >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
        print("Strong password")
        break
    else:
        print("Wrong password")