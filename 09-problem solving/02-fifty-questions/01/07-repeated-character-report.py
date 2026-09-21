s = input("Enter a string: ")
empty_str = ""

for i in s:
    if i not in empty_str:
        count = 0

        for j in s:
            if j == i:
                count += 1

        if count > 1:
            if count == 2:
                print(i, count, "Duplicate")
            elif count <= 4:
                print(i, count, "Repeated")
            else:
                print(i, count, "Highly Repeated")

        empty_str += i