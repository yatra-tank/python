# # Check whether two strings contain the same character frequencies without sorted/set/Counter.
# s1 = input("Enter a string: ").strip().lower()
# s2 = input("Enter another string: ").strip().lower()

# count = 0

# if len(s1) == len(s2):
#     for i in s1:
#         for j in range(len(s2)):
#             if s2[j] == i:
#                 count += 1
                
#                 s2 = s2[:j] + " " + s2[j+1:]
#                 break 

# if count == len(s1) and len(s1) > 0:
#     print("anagram")
# else:
#     print("not an anagram")

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

sum1 = 0
sum2 = 0
len1 = 0
len2 = 0

for char in str1:
    len1 += 1
    sum1 += ord(char)

for char in str2:
    len2 += 1
    sum2 += ord(char)


if len1 == len2 and sum1 == sum2:
    print("Anagram")
else:
    print("Not an Anagram")