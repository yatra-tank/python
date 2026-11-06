# You are given a string S. Count the total number of vowels in it.
s = input("Enter a string: ").lower()
count = 0

for i in s:
    if i in 'aeiou':
        count += 1

print(count)