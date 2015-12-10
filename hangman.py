#!/usr/bin/env python

# Thayne Price - 12/8/2015 - Intro to Unix
# This project makes use of GitHub as its version control.
# In this project, I will implement the game hangman. 
# Then the program will print out a empty gallows with  blanks displayed for the unknow letters of   the word. For each mistake the gallows will be displayed with an additional body part. The         incorrect guesses are listed along with the correct guesses in the corresponding blanks. The user will be  given 6 mistakes before the hangman image is completed and "Game Over: You word was ___________". Otherwise if the game is succesfully finished the player is congratulated and shown the corect word. The words to be guessed are selected at random from the dictionary.

import random

GALLOWS = ['''
+---+
|   |
|
|
|
|
======''','''
+---+
|   |
|   O
|
|
|
======''','''
+---+
|   |
|   O
|   |
|
|
======''','''
+---+
|   |
|   O
|  /|
|
|
======''','''
+---+
|   |
|   O
|  /|\
|
|
======''','''
+---+
|   |
|   O
|  /|\
|  /
|
======''', '''
+---+
|   |
|   O
|  /|\
|  / \
|
======''']

dictionary = 'unix computer programming mouse keyboard notebook coffee mug rocks elephant wallet knife map light monitor desk door laptop chair plastic metal steel evangelical constantinople jarassic incubate contain'.split()

def randomPick(list):
	#randomizes the dictionary string
	index = random.randint(0, len(list)-1)
	return list[index]

def dispGallows(GALLOWS, right, wrong, word):
# This function displays the corresponding gallows image depending on the number of used guesses. 
	print('Remaining Guesses: ' + str(6 - len(wrong)))
	print(GALLOWS[len(wrong)])
	print
	
	#Loop prints the wrong guesses
	print 'Incorrect guesses:', 
	i = 0
	while(i < len(wrong)):
		print wrong[i],
		i = i+1
	print
	
#The display word is filled in as correct guesses are entered	
	displayWord = "_"*len(word)
	
	j = 0
    	while(j < len(word)):
		if word[j] in right:
			displayWord = displayWord[:j] + word[j] + displayWord[1+j:]
		j = j+1
#Outputs the display word to teh screen
	l = 0
	while(l < len(displayWord)):
		print displayWord[l],
		l = l+1 
	print

def getInput(guesses):
# retrieves input and checks that the input is of the correct format. A single letter and that it has not been used before.
	while True:
		print('Input a single letter for your guess')
		guess = raw_input()
		if len(guess) !=  1:
			print('Input can only be a single letter')
		elif guess in guesses:
			print('You have already guessed that! Try something new.')
		else:
			return guess

print('Welcome to Hangman!')
print
print("To play input a single letter. You are allowed 5 wrong guesses.")

wrong = ''
right = ''
word = randomPick(dictionary)


k = 0
while(k <= 6):
	dispGallows(GALLOWS, right, wrong, word)
	
	#Gets input from the user	
	guess = getInput(right + wrong)

	if guess in word:
		right = right + guess
		complete = True
		c = 0
		while(c < len(word)):
			if word[c] not in right:
				complete = False
				break
			c = c+1
		if complete is True:
			print('Congragulations! You figured out the word!')		
			print('Your word was: ' + word)
			break
	else:
		wrong = wrong + guess
		k = k+1
		if len(wrong) == 6:
			dispGallows(GALLOWS, right, wrong, word)
			print('GAME OVER! Your word was: '+  word)
			break
	
