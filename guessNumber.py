import random

guessed_number = random.randrange(1, 100, 1)
def decider (*x) :
	while x != guessed_number :
		x = raw_input("Enter guessed number (from 1 to 100): ")
		print guessed_number
		if x < guessed_number :
			print("Wrong! Guessed number is greater. Try again")
			continue
		elif x > guessed_number :
			print("Not this time fella. Guessed number is smaller. Try again")
			continue
		elif x == guessed_number :
			print("Bingo! You guessed the number. Now go and take a cookie")
			break
decider()



