import time
import random

name = input('Please enter your name: ')
print(f'\nHello {name}, welcome to Hangman!')
time.sleep(1)

words = ['arrow', 'letter', 'christmas', 'computer', 'crocodile', 'leopard', 'highway',
         'shotgun', 'princess', 'dragon', 'beach', 'notebook', 'doctor', 'lawyer', 'gender',
         'balloon', 'carrot', 'spinach', 'message', 'powerful', 'wonderful', 'exciting']

word = random.choice(words)
print('\nYour word is: ')
printed_word = '_' * len(word)
print(printed_word)
no_guesses = 0


def reveal_letters(guessed_letter, revealed_word):
    correct_guess = False

    for i, letter in enumerate(word):
        if letter == guessed_letter:
            revealed_word = revealed_word[:i] + guessed_letter + revealed_word[i + 1:]
            correct_guess = True

    if correct_guess:
        print(f'\n{revealed_word}')
    else:
        print('Wrong guess! Try again.')
        print(f'\n{revealed_word}')

    return revealed_word


while 0 <= no_guesses <= 20:
    guess = input('\nGuess a letter: ')
    printed_word = reveal_letters(guess, printed_word)
    no_guesses += 1

    if printed_word == word:
        print('\nCongrats!')
        break

    if no_guesses >= 20:
        print(f'\nYou are out of guesses.\nThe word was {word}.')
        break
