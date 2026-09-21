for i in range(5):
    password = input("Enter password: ")

    conditions = 0
    upper = False
    lower = False
    digit = False
    special = False

    if len(password) >= 8:
        conditions += 1

    for j in password:
        if j.isupper():
            upper = True
        elif j.islower():
            lower = True
        elif j.isdigit():
            digit = True
        else:
            special = True

    if upper:
        conditions += 1
    if lower:
        conditions += 1
    if digit:
        conditions += 1
    if special:
        conditions += 1

    if conditions == 5:
        print("Strong")
    elif conditions >= 3:
        print("Medium")
    else:
        print("Weak")