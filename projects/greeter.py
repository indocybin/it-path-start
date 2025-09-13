from datetime import datetime
while True:
	name = input("What is your name? (type 'quit' to exit) ")
	if name.lower() == "quit":
		print ("Goodbye, see you next time!")
		break

# ASK FOR USER'S NAME
name = input("What is your name? ")
# GET CURRENT HOUR
current_hour = datetime.now().hour
# DECIDE GREETING BASED ON TIME
if current_hour < 12:
	greeting = "Good morning"
elif current_hour < 18:
	greeting = "Good afternoon"
else:
	greeting = "Good evening"
print (f"{greeting}, {name}! I'm glad you're practicing Python.")
