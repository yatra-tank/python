fail = 0
passed = 0
good = 0
excellent = 0

for i in range(10):
    marks = int(input("Enter marks: "))

    if marks < 35:
        print("Fail")
        fail += 1
    elif marks <= 49:
        print("Pass")
        passed += 1
    elif marks <= 74:
        print("Good")
        good += 1
    else:
        print("Excellent")
        excellent += 1

print("Fail:", fail)
print("Pass:", passed)
print("Good:", good)
print("Excellent:", excellent)