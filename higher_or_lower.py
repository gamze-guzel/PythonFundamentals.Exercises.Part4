from random import randrange

numbers= randrange(1,10)
while True:
    userInput= int(input("Guess a number from 1-10"))
    if userInput > numbers:
        print("Too High")
    elif userInput < numbers:
        print("Too Low")
    elif userInput == numbers:
        print("You got it!")
        break