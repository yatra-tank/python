# For i,j from 1 to 5, print X if i is divisible by j, otherwise -.
for i in range(1, 6):
    for j in range(1, 6):
        if i%j == 0:
            print("X", end= " ")
        else:
            print("-", end= " ")
    print()