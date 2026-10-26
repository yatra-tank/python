# Use nested loops to identify longest and shortest words without max/min.
s = input("Enter a string: ")
word = s.split()

L = []
for i in word:
    length = len(i)
    L.append(length)

print(L)
print(max(L)) 
print(min(L)) 