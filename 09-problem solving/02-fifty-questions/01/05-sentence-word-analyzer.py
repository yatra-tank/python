s = input("Enter a sentence: ")
words = s.split()

short = 0
medium = 0
long = 0

for i in words:
    length = len(i)

    if length <= 3:
        print(i, length, "Short")
        short += 1
    elif length <= 6:
        print(i, length, "Medium")
        medium += 1
    else:
        print(i, length, "Long")
        long += 1

print("Short:", short)
print("Medium:", medium)
print("Long:", long)