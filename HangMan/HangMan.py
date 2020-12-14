import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):

    guessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter + ' '
        else:
            guessedWord += '_ '
    return guessedWord


def getAvailableLetters(lettersGuessed):
    import string
    alpha = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        alpha.remove(letter)
    return ''.join(alpha)

def hangman(secretWord):
    print("Welcome to the game, Hangman!\nI am thinking of a word that is" , len(secretWord) , "letters long.")

    numOfGuesses = 8
    lettersGuessed = []

    while numOfGuesses > 0 and isWordGuessed(secretWord, lettersGuessed) == False :
        print("------------\nYou have",numOfGuesses, "guesses left.")
        print("Available letters: ",getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")

        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
        elif letter in secretWord:
            lettersGuessed += letter
            print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
        else:
            print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
            lettersGuessed += letter
            numOfGuesses -= 1

    if numOfGuesses == 0 :
        print("-----------\nSorry, you ran out of guesses. The word was",secretWord)

    else:
        print("------------\nCongratulations, you won!")



secretWord = "potato"
hangman(secretWord)

