
 Thayne Price - 12/8/2015 - Intro to Unix
 This project makes use of GitHub as its version control.
 In this project, I will implement the game hangman. 
 Then the program will print out a empty gallows with  blanks displayed for the unknow letters of   the word. For each mistake the gallows will be displayed with an additional body part. The         incorrect guesses are listed along with the correct guesses in the corresponding blanks. The user will be  given 6 mistakes before the hangman image is completed and "Game Over: You word was ___________". Otherwise if the game is succesfully finished the player is congratulated and shown the corect word. The words to be guessed are selected at random from the dictionary.

To play:
1. run python ./hangman.py
2. input single letter, this is specified, and there is some input checking
3. You will get 6 tries to fill in the word, if you cannot you are prompted that the game is over. If you succeed you will be congragulated for your success :)

As far as I can tell everything is functioning correctly, except that the gallows image that is printed gets squished for some reason after 3 incorrect guesses.
