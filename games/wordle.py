import random


def game_instruction():
    print("""Wordle is a single player game 
A player has to guess a five letter hidden word 
You have six attempts   
"✅" Indicates that the letter at that position was guessed correctly 
"✔" indicates that the letter at that position is in the hidden word, but in a different position 
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)


game_instruction()


def check_word():
    words = ['jacket', 'supply', 'budget', 'legend', 'series', 'affect', 'moment', 'lounge', 'reward', 'common']
    hidden_word = random.choice(words)
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word: "))
        if guess == hidden_word:
            print("You guessed the word correctly! ")
            break
        else:
            attempt = attempt - 1
            print(f"you have {attempt} attempt(s) ,, \n ")
            for char, letter in zip(hidden_word, guess):
                if letter in hidden_word and letter in char:
                    print(letter + " ✅ ")

                elif letter in hidden_word:
                    print(letter + " ✔ ")
                else:
                    print(" ❌ ")
            if attempt == 0:
                print("Game over")


check_word()
