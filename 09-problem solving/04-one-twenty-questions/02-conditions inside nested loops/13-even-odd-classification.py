# For i and j from 1 to 4, print E when i+j is even, otherwise O.
for i in range(1, 5):
    for j in range(1, 5):
        if (i + j)%2 == 0:
            print("E", end= " ")
        else:
            print("O", end= " ")
    print()