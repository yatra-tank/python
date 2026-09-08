tempt = float(input("Enter temperature in Celsius: "))

if tempt < 0:
    print("Freezing")
elif tempt <= 15:
    print("Very Cold")
elif tempt <= 25:
    print("Cold")
elif tempt <= 35:
    print("Normal")
else:
    print("Hot")