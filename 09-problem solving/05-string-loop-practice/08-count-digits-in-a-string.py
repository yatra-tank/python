# You are given a string S containing lowercase English letters and digits. Count how many digit characters are present in the string. Do not convert the complete string into an integer.
s = input("Enter a string: ")
count = 0

for i in s:
    if i in '0123456789':
        count += 1

print(count)