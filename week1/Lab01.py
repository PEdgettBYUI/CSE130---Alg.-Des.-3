# 1. Name: 
#    Patrick T. Edgett
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#      This program is a simple Guessing Game made in python. Your goal is to guess a random number
#       in the lowest number of attempts.
# 4. What was the hardest part? Be as specific as possible.
#    I'm pretty familiar with if-else comparison statements at this point, but I have never settled
#       on a good name scheme for my variables. It makes it look amateurish. As well as getting the
#       Needed RNG to keep the video length under the maximum 1 minute length requirement can be a hassle.
# 5. How long did it take for you to complete the assignment?
#    Approx. 32 Minutes
# Began: 2:27pm, 4/25 | Concluded: 2:45pm, 4/25 | Video Completed: 2:59pm, 4/25

import random

# Game introduction.
print("\nThis is the \"Guess A Number\" Game!")
      
# Prompt the user for how difficult the game will be. Ask for an integer.
usr_inp = int(input("Pick a positive integer: "))
value_max = usr_inp

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 & {value_max}.")

# Initialize the sentinal and the array of guesses.
guesses_tried = 0
prev_guesses = []
usr_inp = 0

# Play the guessing game.
while usr_inp != value_random:
    # Prompt the user for a number.
    usr_inp = int(input("> "))

    # Store the number in an array so it can be displayed later.
    prev_guesses.append(usr_inp)
    guesses_tried += 1

    # Make a decision: was the guess too high, too low, or just right.
    if usr_inp > value_random:
        print(" Too high!")
    elif usr_inp < value_random:
        print(" Too low!")
# Give the user a report: How many guesses and what the guesses where.
print(f"You were able to find the number in {guesses_tried}.")
print(f"The numbers you guessed were: {prev_guesses}\n\n")