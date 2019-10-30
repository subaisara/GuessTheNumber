# Number Guess game

import random

# pick a secret number
secret = random.randint(1, 99)
guess = 0
tries = 0

print("AHOY!  I'm the Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 99.  I'll give you 6 tries. ")

# try until they guess it or run out of turns
while guess != secret and tries < 6:
    # get the player's guess
    guess = int(input("What's yer guess? "))

    if guess < secret:
        print("Too low, ye scurvy dog!")
    if guess > secret:
        print("Too high, landlubber!")
    # used up one try
    tries = tries + 1

# print message at end of game
if guess == secret:
    print("Avast! Ye got it!  Found my secret, ye did!")
else:
    print("No more guesses!  Better luck next time, matey!")
    print("The secret number was", secret)
