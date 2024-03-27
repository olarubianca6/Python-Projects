from skimage import io
from matplotlib import pyplot as plt
import random
import time


def quiz():

    print('QUIZ: Which Heri are you?')
    time.sleep(2)

    print(f'\nwhich would you rather eat?\n'
          f'1. pickles with caramel\n'
          f'2. deep fried tarantula\n'
          f'3. hot dog spaghetti\n'
          f'4. soy sauce ice cream\n'
          f'5. a raw snail\n')
    answer1 = input('write the number of your answer: ')

    print(f'\nwhat animal would you rather have as a pet?\n'
          f'1. a bear\n'
          f'2. a nest of ants\n'
          f'3. a komodo dragon\n'
          f'4. a bat\n'
          f'5. a cheetah\n')
    answer2 = input('write the number of your answer: ')

    print(f'\nwhat superpower would you rather have?\n'
          f'1. invisibility but every step you take is squeaky\n'
          f'2. flying but everywhere you go there are tree branches getting in your face\n'
          f'3. teleportation but you never choose where you end up\n'
          f'4. you have as much money as you want but everytime you go outside a dog will attack you\n')
    answer3 = input('write the number of your answer: ')

    print(f'\nwho would you rather have as a parent?\n'
          f'1. Vladimir Putin\n'
          f'2. Cersei Lannister\n'
          f'3. Charles Manson\n'
          f'4. Angela Merkel\n'
          f'5. Hannibal Lecter\n')
    answer4 = input('write the number of your answer: ')

    print(f'\nwhat toast are you?\n'
          f'1. plain toast\n'
          f'2. avocado and egg toast\n'
          f'3. french toast\n'
          f'4. nutella and banana toast\n')
    answer5 = input('write the number of your answer: ')

    if answer1 and answer2 and answer3 and answer4 and answer5:
        cats = ["angrycat.jpg", "fatcat.jpg", "happycat.jpg", "sleepycat.jpg"]
        picture = random.choice(cats)
        io.imshow(picture)
        plt.show()


quiz()
