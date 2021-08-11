#Akhil Senthil
#aksenthi@ucsc.edu
#Programming Assignment 4
#This program allows the user to have three guesses to guess a random number ranging from 1 - 10. It gives them clues if it is lower or higher than their guess. 
import random

number = random.randint(1, 10)
guesses = 3
print()
print("I'm thinking of an integer in the range 1 to 10. You have three guesses.")
print()
guess = 0
chance = 'first'
while number != guess and guesses > 0:
	guess = int(input('Enter your ' + chance + ' guess: '))
	guesses -= 1
	if guess < number:
		print('Your guess is too low.')
		print()
		if guesses == 2:
			chance = 'second'
		elif guesses == 1:
			chance = 'third'
	elif guess > number:
		print('Your guess is too high.')
		print()
		if guesses == 2:
			chance = 'second'
		elif guesses == 1:
			chance = 'third'
	else:
		print('You win!')
		print()

if guess != number:
	print('You lose. The number was ' + str(number) + '.')
	print()