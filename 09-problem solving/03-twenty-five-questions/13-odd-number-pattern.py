# n = int(input("Enter your number: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(2 * j - 1, end=" ")
#     print("")

n = int(input("Enter your number: "))
for i in range(n):
    for j in range(2 * i + 2):
        if j%2 != 0:
            print(j, end=" ")
    print()