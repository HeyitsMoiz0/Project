
import random
print('''
Rules:
    The guess must be 5 characters long.
    You have 10 guesses to guess the word.
''')
# These are the words which will be selected for the wordle.
# If You want you can remove or add words in this code.
word =  ["apple", "grape", "pearl", "stone", "crane", "flame", "tiger","zebra", "chair", "table",
        "piano", "brave", "sword", "cloud", "dream", "flock", "giant", "heart", "ivory", "jelly",
        "knife", "lemon", "mango", "noble", "ocean", "peach", "queen", "raven", "sheep", "toast",
        "umbra", "vivid", "whale", "xenon", "yacht", "zesty", "bloom", "chess", "drain", "eagle",
        "frost", "grind", "haste", "inbox", "jumpy", "kneel", "laugh", "mocha", "night", "orbit",
        "plush", "quake", "rough", "shiny", "trace", "unity", "vapor", "wrist", "yield", "zonal",
        "blink", "candy", "dizzy", "ember", "flora", "gloom", "honey", "image", "joker", "kites",
        "lunar", "march", "nurse", "olive", "pride", "quiet", "river", "sunny", "treat", "vocal",
        "witty", "xylem", "yummy", "angel", "beach", "coral", "daisy", "eager", "fancy", "glove",
        "happy", "index", "jolly", "koala", "leash", "minty", "ninth", "opine", "pasta", "quill"]

word = random.choice(word)

first = word[0]
second = word[1]
third = word[2]
fourth = word[3]
fifth = word[4]

guesses = 0
print(f'The Word is {len(word)} letters long.')

while True:
    try:
        print("Your Guesses",guesses)
        guess = input("Guess The Word: ")

        word1_guess = guess[0]
        word2_guess = guess[1]
        word3_guess = guess[2]
        word4_guess = guess[3]
        word5_guess = guess[4]

        if len(guess) != len(word):
            print("The Guesses must have the same length.")
            continue


        if guess.lower() == word:
            print('You Won! :)')
            print("The word was", word)
            exit()
# If you want to increase the guesses, then remove the number
# '10' below and change it to the amount of guesses you want.
        if guesses == 10:
                print('You Lost! :(')
                print("The word was", word)
                exit()


        if guess.lower() != word:
                guesses += 1

# Below this, is the code used for finding out if
# you got the word or not and for finding green and yellow.

        if first == word1_guess:
            print(word1_guess,"correct")

        elif first in guess :
            print(word[0],'Yellow')

        if second == word2_guess:
            print(word2_guess,"correct")

        elif second in guess :
            print(word[1],'Yellow')

        if third == word3_guess:
            print(word3_guess,"correct")

        elif third in guess :
            print(word[2],'Yellow')

        if fourth == word4_guess:
            print(word4_guess,"correct")

        elif fourth in guess :
            print(word[3],'Yellow')

        if fifth == word5_guess:
            print(word5_guess,"correct")

        elif fifth in guess :
            print(word[4],'Yellow')

    except IndexError:
        print('Guess must be 5 characters long.')




