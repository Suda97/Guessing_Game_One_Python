import random

i = 1
while True:
    num = random.randint(1, 9)
    uGuess = input("Game number: " + str(i) + "\nIf You want to quit type 'quit'. \nIf you want to play type the "
                                              "number from 1 to 9: ")
    if uGuess == 'quit':
        print("\nYou played " + str(i - 1) + " games. \nBye, bye!")
        break
    elif int(uGuess) == num:
        print("\nNice one! You guessed it!\n")
    elif int(uGuess) > num:
        print("\nToo high! :(\n")
    elif int(uGuess) < num:
        print("\nToo low! :(\n")
    i = i + 1
