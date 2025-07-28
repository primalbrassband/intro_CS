# -*- coding: utf-8 -*-
"""
Created on Thu May  1 18:25:24 2025

@author: willt
"""

import random


# step 0: choose game mode
def get_numbers(mode):
    """Return a sorted list of 5 numbers based on game mode."""
    if mode == "static":
        numbers = [150, 400, 700, 850, 999]
    else:  # random mode
        numbers = random.sample(range(1, 1001), 5)
    numbers.sort()
    return numbers


# step 1: game starts
print("Welcome to the guessing game.")
print("Would you like static or random?")

# step 2: game loop


while True:
    mode = input("Type static or random: ").strip().lower()
    if mode in ['static', 'random']:
        break
    print("Invalid, enter static or random.")

numbers = get_numbers(mode)
print("I'm thinking of 5 numbers between 1 and 1000.")

previous_distance = None
incorrect_guess = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer. ")
        continue

    if guess in numbers:
        print("Success!")
        print(incorrect_guess, "incorrect guesses")
        break

    # find closest number in list
    closest = min(numbers, key=lambda x: abs(x - guess))
    current_distannce = abs(closest - guess)

    # feedback
    if previous_distance is None:
        print("Wrong, try again.")
    else:
        if current_distannce < previous_distance:
            print("Getting warmer.")
        elif current_distannce > previous_distance:
            print("Getting colder.")
        else:
            print("That's the same distance as before.")

    previous_distance = current_distannce
    incorrect_guess += 1

    # hint feature
    if incorrect_guess == 3:
        margin = 10
        lower = max(1, closest - margin)
        upper = min(1000, closest + margin)
        print(f"Hint: the closest number is between {lower} and {upper}")
