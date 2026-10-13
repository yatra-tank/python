# Take a string and a target character. Scan the string from left to right. Print each character as it is checked. Stop immediately after finding the target. If the target does not appear, check the entire string.
s = input("Enter a string: ")
target = input("Enter your target character: ")

for i in s:
    print(i)
    if i == target:
        break