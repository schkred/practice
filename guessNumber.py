import random

x = raw_input("Enter guessed number: ")
guessed_number = random.randrange(1, 100, 1)
if x < guessed_number :
	print("Wrong! Guessed number is greater. Try again")
elif x > guessed_number :
	print("Not this time! Guessed number is smaller. Try again")
elif x == guessed_number :
	print("Bingo! You guessed the number. Now go and take a cookie")


