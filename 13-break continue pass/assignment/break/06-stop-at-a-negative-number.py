# Given a sequence of integers, print numbers from left to right and stop when the first negative number is encountered. Do not print the negative number.
storage = ''

while True:
    numbers = int(input('Enter a number: '))

    if numbers < 0:
        break
    else:
        storage += str(numbers) + ' '

print(storage)