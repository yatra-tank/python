# Given marks separated by spaces, print only marks that are at least 40. Use continue to skip marks below 40.
n = input("Enter marks separated by spaces: ").split()

for i in n:
    i = int(i)

    if i < 40:
        continue

    print(i, end=" ")