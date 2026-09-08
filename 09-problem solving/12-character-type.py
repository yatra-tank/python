ch = input("Enter one character: ")

if ch >= "A" and ch <= "Z":
    print("Uppercase alphabet")
elif ch >= "a" and ch <= "z":
    print("Lowercase alphabet")
elif ch >= "0" and ch <= "9":
    print("Digit")
else:
    print("Special character")