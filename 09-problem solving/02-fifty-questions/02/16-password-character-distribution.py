s = input("Enter your password: ")

uppercase = 0
lowercase =0
digits = 0
special = 0

for i in s:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
    elif i.isdigit():
        digits += 1
    else:
        special += 1

print("Uppercase:", uppercase / len(s) * 100)
print("Lowercase:", lowercase / len(s) * 100)
print("Digits:", digits / len(s) * 100)
print("Special:", special / len(s) * 100)