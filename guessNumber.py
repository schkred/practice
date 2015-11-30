import random

guessed_number = random.randrange(1, 100, 1)
def decider (*x) :
	while x != guessed_number :
		x = int(raw_input("Enter guessed number (from 1 to 100): "))
		if x < guessed_number :
			print("Wrong! Guessed number is greater. Try again")
		elif x > guessed_number :
			print("Not this time fella. Guessed number is smaller. Try again")
		elif x == guessed_number :
			print("Bingo! You guessed the number. Now go and take a cookie")
decider()



