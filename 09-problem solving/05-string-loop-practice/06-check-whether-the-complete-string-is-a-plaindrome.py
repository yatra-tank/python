# You are given a string S. Check whether the complete string is a palindrome.
s = input("Enter a string: ")

left = 0
right = len(s) - 1
ok = True

while left < right:
    if s[left] != s[right]:
        ok = False
        break
    left += 1
    right -= 1

if ok:
    print("yes")
else:
    print("no")