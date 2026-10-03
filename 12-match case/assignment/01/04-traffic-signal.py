# Take a traffic signal color as input:

# red
# yellow
# green
# Use match-case to display:

# red    → Stop
# yellow → Wait
# green  → Go

print("""--- TRAFFIC SIGNAL ---
1. RED
2. YELLOW
3. GREEN""")

n = input("Enter your order: ").lower().strip()

match n:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")