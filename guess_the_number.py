import random

restart_game = False
secret_number = random.randint(1, 10)
not_guessed = True
number_of_guesses = 5

print "I am thinking of a number between 1 and 10."
while not_guessed:
	guessed_number = raw_input("What's the number? ")
	if (int(guessed_number) > secret_number):
		print "Nope, %s is too high." % guessed_number
		number_of_guesses -= 1
		print "You have %s guesses left." % number_of_guesses
		if (number_of_guesses == 0):
			print "Sorry, You are out of guesses."
			not_guessed = False
			restart_game = True
			# restart = raw_input("Would you like to play again (y/n)? ")
			# if (restart == "y" or restart == "yes"):
			# 	not_guessed = True
			# 	number_of_guesses = 5
			# elif (restart == "n" or restart == "no"):
			# 	print "Goodbye!"
			# else:
			# 	print "TROLOLOLOLOLOL... Goodbye."
	elif (int(guessed_number) < secret_number):
		print "Nope, %s is too low." % guessed_number
		number_of_guesses -= 1
		print "You have %s guesses left." % number_of_guesses
		if (number_of_guesses == 0):
			print "Sorry, You are out of guesses."
			not_guessed = False
			restart_game = True
			# restart = raw_input("Would you like to play again (y/n)? ")
			# if (restart == "y" or restart == "yes"):
			# 	not_guessed = True
			# 	number_of_guesses = 5
			# elif (restart == "n" or restart == "no"):
			# 	print "Goodbye!"
			# else:
			# 	print "TROLOLOLOLOLOL... Goodbye."
	elif (int(guessed_number) == secret_number):
		print "You WIN!"
		not_guessed = False
		restart_game = True
		# restart = raw_input("Would you like to play again (y/n)? ")
		# if (restart == "y" or restart == "yes"):
		# 	not_guessed = True
		# 	number_of_guesses = 5
		# elif (restart == "n" or restart == "no"):
		# 	print "Goodbye!"
		# else:
		# 	print "TROLOLOLOLOLOL... Goodbye."
	while restart_game:
		play_again = raw_input("Would you like to play again (y/n)?: ")
		if (play_again == "y" or play_again == "yes"):
			restart_game = False
			not_guessed = True
			number_of_guesses = 5
			secret_number = random.randint(1, 10)
		elif (play_again == "n" or play_again == "no"):
			print "Goodbye!"
			restart_game = False
		else:
			print "TROLOLOLOLOLOLOLOL... Goodbye."
			restart_game = False































