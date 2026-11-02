# Your are given an integer N. Your task is to check whether the string "420" is present in its decimal representation.
def check(N):
    s = str(N)

    if "420" in s:
        print("Caught")
    else:
        print("Escaped")

N = int(input("Enter a number: "))
check(N)