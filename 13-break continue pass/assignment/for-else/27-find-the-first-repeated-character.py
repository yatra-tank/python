s = input("Enter a string: ")

for i in s:
    if s.count(i) >= 2:
        print(i)
        break
else:
    print("No repeated character")