# For every character, print it with repetition numbers 0,1,2.
s = input("Enter a string: ")

for i in s:
    for j in range(3):
        print(i, j)