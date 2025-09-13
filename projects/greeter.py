from datetime import datetime
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
print (f"{greeting}, {name}! Welcome to your python journey.")
