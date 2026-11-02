# Use nested loops to identify longest and shortest words without max/min.
# s = input("Enter a string: ")
# word = s.split()

# L = []
# for i in word:
#     length = len(i)
#     L.append(length)

# print(L)
# print(max(L)) 
# print(min(L)) 

s = input("Enter a string: ")
word = s.split()

longest = word[0]
shortest = word[0]

for i in word:
    length = 0

    for j in i:
        length += 1

    if length > len(longest):
        longest = i

    if length < len(shortest):
        shortest = i

print(longest)
print(shortest)