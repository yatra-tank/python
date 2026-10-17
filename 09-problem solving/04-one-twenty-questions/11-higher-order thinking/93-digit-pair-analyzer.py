# Extract digits and classify every ordered digit pair.
s = input("Enter a string: ")

for i in range(len(s)):
    for j in range(len(s)):
        if i != j:
            if s[i] > s[j]:
                print("Descending:", end= " ")
                print(s[i], s[j])

            elif s[i] < s[j]:
                print("Ascending:", end= " ")
                print(s[i], s[j])

            else:
                print("Equal:", end= " ")
                print(s[i], s[j])