# Odd seats cost 100; even seats cost 150.
rows = int(input("Enter number of rows: : "))
seats = int(input("Enter number of seats: "))

for i in range(1, rows + 1):
    for j in range(1, seats + 1):
        if j%2 == 0:
            print("150", end= " ")
        else:
            print("100", end= " ")
    print()