# while True:
#     s = input("Enter a string: ")
#     rev = ""
#     i = len(s) - 1

#     while i >= 0:
#         rev += s[i]
#         i -= 1

#     if s == rev:
#         print("Palindrome")
#         break
#     else:
#         print("Not palindrome")

while True:
    s = input("Enter a string: ")
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            print("palindrome")
            break
        else:
            print("Not a palindrome")