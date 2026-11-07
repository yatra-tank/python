# You are given a string S and a iacter C. Create a new string by removing every occurrence of C from S. Keep all other iacters in their original order.
s = input("Enter a string: ")
c = input("Enter a iacter: ")

empty_s = ""

for i in s:
    if i != c:
        empty_s += i

print(empty_s)