text = input("Enter a string: ")

upper = 0
lower = 0
digit = 0
space = 0
special = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch == " ":
        space += 1
    else:
        special += 1

highest = max(upper, lower, digit, space, special)

if [upper, lower, digit, space, special].count(highest) > 1:
    print("Tie")
elif upper == highest:
    print("Uppercase")
elif lower == highest:
    print("Lowercase")
elif digit == highest:
    print("Digits")
elif space == highest:
    print("Spaces")
else:
    print("Special Characters")