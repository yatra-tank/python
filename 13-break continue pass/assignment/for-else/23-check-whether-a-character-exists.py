# Take a string and a target character. Use for-else to print "Character exists" if found, or "Character missing" otherwise.
s = input("Enter a string: ")
target = input("Enter the target character: ")

for i in s:
    if i == target:
        print("Character exists")
        break
else:
    print("Character missing")