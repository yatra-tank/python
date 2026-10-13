# Take a list of integers and a target number. If the target exists, print "Found". Otherwise, print "Not found" using for-else.
n = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter the target number: "))

for i in n:
    if i == target:
        print("Found")
        break
else:
    print("Not found")