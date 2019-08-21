import random

correct_number = random.randint(1, 10)

uname = str(input("What is your name?  "))

print("Hello, ", uname + ".")

game_start = str(input("Would you like to play a guessing game?  [y/n]  "))

if game_start == "y":
    print()
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    start = True
elif game_start == "n":
    print("Ok then, maybe next time.  ")
    start = False
else:
    print("That's not one of the options. [y/n]  ")
    start = False

 
while start:
    print()
    guess = int(input("What number am I thinking of?  "))
    if guess == correct_number:
        print("Good job. You win.")
        start = False
    elif guess != correct_number:
        print("That's not right. Try again.")
        print()




