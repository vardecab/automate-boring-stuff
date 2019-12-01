# Guess a number game.

import random

print("Hello :) What's your name?")

# TODO: add while loop checking if input is string not number

try:
    # player_name = int(input())
    # print("That doesn't sound like a name 🤔")
    player_name = input()
    print("Well, hello", player_name.capitalize() + "!")
except ValueError:
    print()

secret_number = random.randint(1,77)
print("I'm thinking of a number between <1 and 77>.")
for guessesTaken in range (1,11):
    print("Take a guess 👀")
    guess = int(input())
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else: 
        break

if guess == secret_number:
    print("Well done " + player_name.capitalize() + "! You won by trying " + str(guessesTaken) + " times 🏆  The secret number was indeed " + str(secret_number) + '.')
else: 
    print("Oh, you just lost 😢  The number I had in mind was " + str(secret_number) + ".")

# print("You took" + str(guessesTaken) + "guesses.")