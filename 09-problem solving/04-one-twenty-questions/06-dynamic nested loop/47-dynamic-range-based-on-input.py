# For i=0..N-1, run range(i).
n = int(input("Enter a number: "))
for i in range(n):
    if i == 0:
        print("i=0 produces no inner output;")
    else:
        for j in range(i):
            print(j, end=" ")
        print()