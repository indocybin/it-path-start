from datetime import datetime

while True:
    name = input("What is your name? (type 'quit' to exit) ")

    if name.lower() == "quit":
        print("Goodbye, see you next time!")
        break   # 👈 after this, NOTHING else in the loop runs

    # 👇 everything below here only runs if name != "quit"
    current_hour = datetime.now().hour

    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}, {name}! I'm glad you're practicing Python.")
