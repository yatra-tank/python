ch = input("Enter one character: ").lower()

if ch >= "a" and ch <= "z":
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")