import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words = 'aguila araña ballena burro camello canguro cebra cisne cobra conejo coyote cuervo elefante gato grillo hornero jirafa koala leon llama mariposa murcielago orangutan oveja panda perro rana rata salmon sapo serpiente siervo tiburon tigre tortuga wombat zorro'.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Letras que ya elegiste y no están --->', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Qué letra elegís?')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Ingresá sólo una letra.')
        elif guess in alreadyGuessed:
            print('Ya habías elegido esa letra. Elegí otra.')
        elif guess not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Tenés que elegir una LETRA.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Querés seguir jugando a este juego? (si o no)')
    return input().lower().startswith('s')



def main():
	
	print('---[[[ A H O R C A D O ]]]---')
	missedLetters = ''
	correctLetters = ''
	secretWord = getRandomWord(words)
	gameIsDone = False

	while True:
		displayBoard(missedLetters, correctLetters, secretWord)

		# Let the player enter a letter.
		guess = getGuess(missedLetters + correctLetters)

		if guess in secretWord:
			correctLetters = correctLetters + guess

			# Check if the player has won.
			foundAllLetters = True
			for i in range(len(secretWord)):
				if secretWord[i] not in correctLetters:
					foundAllLetters = False
					break
			if foundAllLetters:
				print('Si! La palabra secreta es "' + secretWord + '"! GANASTE!')
				gameIsDone = True
		else:
			missedLetters = missedLetters + guess

			# Check if player has guessed too many times and lost.
			if len(missedLetters) == len(HANGMAN_PICS) - 1:
				displayBoard(missedLetters, correctLetters, secretWord)
				print('Se acabaron los intentos!\nFueron ' + str(len(missedLetters)) + ' intentos fallidos y ' + str(len(correctLetters)) + ' letras acertadas. La palabra era "' + secretWord + '"')
				gameIsDone = True

		# Ask the player if they want to play again (but only if the game is done).
		if gameIsDone:
			if playAgain():
				missedLetters = ''
				correctLetters = ''
				gameIsDone = False
				secretWord = getRandomWord(words)
			else:
				break
				
if __name__ == '__main__':
    main()
