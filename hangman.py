#!/usr/bin/env python

# Thayne Price - 12/8/2015 - Intro to Unix
# This project makes use of GitHub as its version control.
# In this project, I will implement the game hangman. Initially the user will be allowed to select 
# the difficulty by typing in easy/medium/hard. Then the program will print out a empty gallows with # blanks displayed for the unknow letters of the word. For each mistake the gallows will be displayed# with an additional body part. The user will be given 5 mistakes before the hangman image is
# completed and "Game Over: You word was ___________". The words to be guessed are selected at random
# from an input file.

import random

GALLOWS = ['''

+---+
|   |
|
|
|
|
=====''','''

+---+
|   |
|   O
|
|
|
=====''','''

+---+
|   |
|   O
|   |
|
|
=====''','''

+---+
|   |
|   O
|  /|
|
|
=====''','''

+---+
|   |
|   O
|  /|\
|
|
=====''','''

+---+
|   |
|   O
|  /|\
|  /
|
=====''', '''

+---+
|   |
|   O
|  /|\
|  / \
|
=====''']

dictionary = 'unix computer programming mouse keyboard notebook coffee mug rocks elephant wallet knife map light monitor desk door laptop chair plastic metal steel evangelical constantinople jarassic incubate contain'.split()

def randomPick(list):
	#randomizes the dictionary string
	index = random.randint(0, len(list)-1)
	return list[index]

def dispGallows(GALLOWS, right, wrong, word)
	print("Guess # ", len(wrong))
	print(GALLOWS[len(wrong)])
	print()
	
	#Loop prints the wrong guesses
	print("Incorrect guesses:", end='')
	i = 0
	while(i < len(wrong)):
		print(wrong[i], end=' ')
		print()
		
	displayWord = "_"*len(word)
	
	j = 0
    	while(j < len(word)):
		if word[j] in right
			displayWord = displayWord[:j] + word[j] + displayWord[1+j:]

def getInput(guesses):
	print('Input a single letter for your guess')
	guess = input()
	return guess

print("Welcome to Hangman!")
print()
print("To play input a single letter. You are allowed 5 wrong guesses.")

wrong = ''
right = ''
word = randomPick(dictionary)
gameOver = False

k = 0
while(k < 5):
	dispGallows(GALLOWS, right, wrong, word)
	
	#Gets input from the user	
	guess = getInput(right + wrong)

	if guess in word:
		right = right + guess
		
	else:
		wrong = wrong + guess
		k = k+1
		if len(wrong) == 5:
			dispGallows(GALLOWS, right, wrong, word)
			print("GAME OVER! Your word was: ", word)
	
