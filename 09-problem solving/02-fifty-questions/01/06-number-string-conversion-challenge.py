for i in range(5):
    n = int(input("Enter a number: "))
    text = str(n)

    even = 0
    odd = 0

    for j in text:
        if j.isdigit():
            if int(j) % 2 == 0:
                even += 1
            else:
                odd += 1

    print("Even digits:", even)
    print("Odd digits:", odd)

    if even > odd:
        print("Even")
    elif odd > even:
        print("Odd")
    else:
        print("Equal")