import random

random_number = random.randint(1, 10)
number_of_guesses = 6
go_again = True
restart_game = False

print "I am thinking of a number between 1 and 10."
while (go_again == True) and (number_of_guesses > 1):
	guess_input = raw_input("What's the number? ")
	if (int(guess_input) > random_number):
		print "Nope, %s is too HIGH." % guess_input
		number_of_guesses -= 1
		print "You have %s guesses left." % (number_of_guesses - 1)
	if (int(guess_input) < random_number):
		print "Nope, %s is too LOW." % guess_input
		number_of_guesses -= 1
		print "You have %s guesses left." % (number_of_guesses - 1)
	if (int(guess_input) == random_number):
		print "YOU WIN!!!"
		go_again = False
		restart_game = True
	while restart_game or (number_of_guesses == 1):
		play_again = raw_input("Would you like to play again (y/n)?: ")
		if (play_again == "y" or play_again == "yes"):
			restart_game = False
			go_again = True
			number_of_guesses = 5
			random_number = random.randint(1, 10)
			print "I am thinking of a number between 1 and 10."
		elif (play_again == "n" or play_again == "no"):
			print "Goodbye!"
			restart_game = False
			number_of_guesses = 0
		else:
			print "TROLOLOLOLOLOLOLOL... Goodbye."
			restart_game = False
			number_of_guesses = 0

		# if (restart_game == "y") or (restart_game == "yes"):
		# 	number_of_guesses = 5
		# elif (restart_game == "n") or (restart_game == "no"):
		# 	print "Goodbye!!!"
		# 	go_again = False
		# else:
		# 	print "TROLOLOLOLOLOL... Goodbye."
		# 	go_again = False
